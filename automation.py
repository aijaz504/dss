#!/usr/bin/python3

import os
import sys
import random
import subprocess
from pathlib import Path

f = open('output.txt','w')

	
def Checker():
	if os.path.exists("Configuration/Agreement.txt"):
            pass
	else:
            Agree.One_time.Agreement()

option = "(1)Scan .tar files\n(2)Scan Images Directly\n(3)Find Total Exclusive CVEs\n(4)Count CVE\n(9)EXIT"
options = str(option)
print(options)
sce = int(input("\n[Give-Input:]" + "-->"))

if sce == 1:
	cwd = os.getcwd()
	em=str(input("Enter path of .tar file:"))
	strA='grype ' +em
	returned_value = subprocess.call(strA, shell=True)  
	#print('returned value:', returned_value)
	
	print("\nTRIVY SCAN")
	print("\n")
	
	strB ='trivy image -i '+em
	returned_value = subprocess.call(strB, shell=True) 
	#print('returned value:', returned_value)
	
	print("\nSNYK SCAN")
	print("\n")
	
	
	strC = 'snyk container test docker-archive:'+em+'--json'
	returned_value = subprocess.call(strC, shell=True) 
	print('returned value:', returned_value)
	
	view=str(input("Do you want list of Exclusive(y/n):"))
	if view=="y":
		ask=str(input("Put path of file to find exclusive CVEs(Onlt 3 files accepted):\n"))
		str3="python3 cve2.py "+ask
		os.system(str3)
	else:
		quit()	
	
elif sce==2:
	em=str(input("Enter Name of image:"))
	#str2="grype "+em
	str3="trivy image "+em
	str4="snyk container test "+em+ " --json"
	cmd = "docker rm clair ; docker rm db"
	d = os.popen("docker stop clair ; docker stop db; docker rm clair ;  docker rm db ; docker run -p 5432:5432 -d --name db arminc/clair-db:latest ; docker run -p 6060:6060 --link db:postgres -d --name clair arminc/clair-local-scan:latest" )
	dd=d.read()
	print(dd)
	str5="./clair_scan --ip=192.168.174.132 "+em
	#os.system(str2)
	os.system(str3)
	os.system(str4)
	os.system(str5)
	view=str(input("Do you want list of Exclusive(y/n):"))
	if view=="y":
		ask=str(input("Put path of file to find exclusive CVEs:\n"))
		str3="python3 cve2.py "+ask
		os.system(str3)
	else:
		quit()	
		
elif sce==3:
	ask=str(input("Put path of files to find exclusive CVEs(input 4 path):"))
	str3="python3 cve2.py "+ask
	os.system(str3)
	print("\n")
	
		
elif sce==4:
	ask=str(input("Put path of file to find number of CVEs:"))
	str4="python3 cveCounter.py "+ask
	os.system(str4)
	print("\n")
	
elif sce==9:
	quit()



	
		                   
                    
                    
