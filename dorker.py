# GoogD0rker by sosto

from googlesearch import search
import os
import argparse
from random import randint
from time import sleep


# Add in argument options
parser = argparse.ArgumentParser(description='Domain to target')
parser.add_argument('-d', action='store', dest='domain',
                    help='only the domain you want to target')

results = parser.parse_args()

# 
if results.domain == None:
	print ("Please enter the domain you wish to target: main.py -d target.com")
	exit()
else:
	domain = results.domain



def google_it (domain,dork,filename):
	out=open(filename,"a")
	for title in search(dork, stop=50):
            	print(title)
            	out.write(title)
            	out.write("\n")
	out.close()
	



print ("Check GHDB for "+domain+"\n")
with open("payloads", 'rb') as payloads:
	for p in list(payloads.readlines()):
		print '---Checking for -----'+ p
		try:
			google_it (domain, "domain:*."+domain+ " "+ p,domain)
		except:
			pass
		sleep(randint(1,3))