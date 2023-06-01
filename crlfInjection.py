import sys
import requests
from subprocess import Popen,PIPE
print("\033[1;32m")
run=Popen("figlet CRLF Injection",shell=True,stdout=PIPE,stderr=PIPE)
print(run.stdout.read().decode())
class MyTools:
	def __init__(self,url):
		self.url = url
	def CRLF(self):
		url = self.url
		f=open("wordlist.txt","r")
		for evil in f:
			req=requests.get(f"{url}/{evil}")
			header="Header-Test" #add header check
			if header in req.headers:
			    print(f"vulnerable {url}")
			else:
          		    print(f"Not vulnerable {url}")


if sys.argv[1]:
    MyTools(sys.argv[1]).CRLF()
else:
    print("\033[1;31m"+"Oooh! Not found Argument [crlfinjection.py http://test.com]")
