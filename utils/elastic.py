
import shodan
from elasticsearch import Elasticsearch
from elasticsearch.client import IndicesClient
from utils.color import Colors

import logging
logging.basicConfig(level=logging.ERROR)

def search (api=None, dork=None, limit=None, offset=None) :

	data = []

	try:

		api = shodan.Shodan(api)
		res = api.search(dork, limit=limit, offset=offset)

		matches = res['matches']
		total = res['total']

		for match in matches:

			ipaddress = match['ip_str']
			port = match['port']
			org = match['org']
			location = match['location']
			domains = match['domains']
			hostnames = match['hostnames']

			info = {
				'ipaddress': ipaddress,
				'port': port,
				'org': org,
				'location': location,
				'domains': domains,
				'hostnames': hostnames,
			}

			data.append(info)
                
	except shodan.APIError as error:
		print(error)

	return data

def analyze(data=None, http_auth=None, timeout=None) :

	""" returns a list of objects with possible indices containing relevant information. """

	ipaddress = data['ipaddress']
	port = data['port']
	domains = data['domains']
	org = data['org']
	hostnames = data['hostnames']
	city = data['location']['city']
	country = data['location']['country_name']

	hostname = ', '.join(str(hostname) for hostname in hostnames)
	domain = ', '.join(str(domain) for domain in domains)

	http = 'http://{}:{}'.format(ipaddress, port)

	elastic = Elasticsearch(hosts=http, timeout=timeout)

	connected = elastic.ping()

	client = IndicesClient(elastic)

	color = Colors()

	# Interesting indexes
	indices = [

	'customer', 
	'profiles', 
	'users', 
	'transfers', 
	'exchanges',
	'api', 
	'payment', 
	'address', 
	'book', 
	'registration', 
	'register', 
	'subscribe', 
	'registry', 
	'patient',
	'email', 
	'passwords', 
	'user', 
	'backup', 
	'config', 
	'contacts', 
	'logins', 
	'customers', 
	'clientes', 
	'clients', 
	'database', 
	'messages', 
	'transactions',
	'client',
	'enderecos',
	'documento',
	'documentos',
	'aplicativo',
	'json',
	'digital',
	'apps',
	]

	keywords = []
	
	try:

		for k, keyword in enumerate(indices):

			# Testing the elastic server is online.
			if not connected:
				continue

			if client.exists(keyword):
				keywords.append(keyword)

	except Exception as error:
		print("Error %s " % (error))

	if len(keywords) > 0:

		keyword = ', '.join(str(keyword) for keyword in keywords)
		print("[+] Interesting indexes were found {}".format( color.error(keyword)))

		print("""
\tBrowser: {}
\tOrganization: {}
\tHostnames: {}
\tDomains: {}
\tCity: {}
\tCountry: {}
\tStatus: Without authentication ({})\n
		""".format(http, org, hostname, domain, city, country, color.status('Open')))