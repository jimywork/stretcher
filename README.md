# Stretcher
Stretcher is a tool to search for open elasticsearch servers.


```

Usage: python stretcher.py --shodan {key}  --action analyze --threads {0..100} --dork 
       python stretcher.py  --help 
   _____ __            __       __             
  / ___// /_________  / /______/ /_  ___  _____
  \__ \/ __/ ___/ _ \/ __/ ___/ __ \/ _ \/ ___/
 ___/ / /_/ /  /  __/ /_/ /__/ / / /  __/ /    
/____/\__/_/   \___/\__/\___/_/ /_/\___/_/     
                                               


 Tool designed to help identify incorrectly
 Applications that are exposing sensitive

    
[+] Interesting indexes were found payment, address, email, user

	Browser: http://34.224.104.129:80
	Organization: Amazon.com
	Hostnames: ec2-34-224-104-129.compute-1.amazonaws.com
	Domains: amazonaws.com
	City: Ashburn
	Country: United States
	Status: Without authentication (Open)

```
  ### Installation
  
```
$ cd $HOME/
$ git clone https://github.com/6IX7ine/stretcher/
$ sudo chmod -R 777 stretcher/
```

### Disclaimer
Code samples are provided for educational purposes. Adequate defenses can only be built by researching attack techniques available to malicious actors. Using this code against target systems without prior permission is illegal in most jurisdictions. The authors are not liable for any damages from misuse of this information or code.
