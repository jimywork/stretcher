#!/usr/bin/env python3

# -*- coding: utf-8 -*-



import argparse
import sys

from datetime import datetime
from pyfiglet import Figlet
from concurrent.futures import ThreadPoolExecutor

from utils.elastic import search
from utils.elastic import analyze


def main():

	graph = Figlet(font='slant').renderText('\tStretcher')
	print(graph)
	print("""
 Tool designed to help identify incorrectly
 Applications that are exposing sensitive
    """)

	parser = argparse.ArgumentParser(description='Stretcher', usage=None)

	parser.add_argument('--dork', required=False, default='product:"Elastic" port:"9200"', help='port:"9200" Elastic')

	parser.add_argument('--shodan', required=True, help='shodan access key.')

	parser.add_argument('--limit', type=int, default=300, required=False, help='limit of results')

	parser.add_argument('--timeout', type=float, required=False, default=1, help='connection timeout')

	parser.add_argument('--threads', type=int, required=False, default=1, help='number of threads')

	parser.add_argument('--action', type=str, required=False, default='analyze', choices=['analyze'], help='action')
	
	args = parser.parse_args()

	if len(sys.argv) <= 2:
		parser.print_help()

	with ThreadPoolExecutor(max_workers=args.threads) as executor:

		try:

			urls = search(api=args.shodan, dork=args.dork, limit=args.limit)
		
			if args.action == 'analyze':
				action = executor.map(analyze, urls, timeout=args.timeout)

		except exception.concurrent.futures.TimeoutError as error:
			print(error)

if __name__ == '__main__':
	main()
	
