#!/usr/bin/python3

import os
import sys
import random
from subprocess import PIPE, run
from pathlib import Path


	
def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

def Checker():
	if os.path.exists("Configuration/Agreement.txt"):
            pass
	else:
            Agree.One_time.Agreement()

option = "(1)Scan .tar file\n(2)Scan Images Directly\n(3)Find Total Exclusive CVEs(4 files)\n(4)Count number of CVEs\n(5)Find Common and Exclusive CVEs(2 files)\n(9)EXIT"
options = str(option)
print(options)
sce = int(input("\n[Give-Input:]" + "-->"))

if sce == 1:

	em=str(input("Enter path of .tar file:"))
	
	file = open('grype.txt','w')
	strA='grype ' +em
	os.system(strA)
	my_output = out(strA)
	file.write(""+my_output)  
	file.close()
	
	print("\nTRIVY SCAN")
	print("\n")
	
	strB ='trivy image -i '+em
	file = open('trivy.txt','w')
	os.system(strB)
	my_output1 = out(strB)
	file.write(""+my_output1)  
	file.close()
	
	print("\nSNYK SCAN")
	print("\n")
	
	
	strC = 'snyk container test docker-archive:'+em+ ' --json'
	file = open('snyk.txt','w')
	os.system(strC)
	my_output3 = out(strC)
	file.write(""+my_output3)  
	file.close()
	
	
	view=str(input("Do you want list of Exclusive CVEs(y/n):"))
	if view=="y":
		#ask=str(input("Put name of text file(example - grype.txt trivy.txt snyk.txt:\n"))

		str3="python3 cve3.py /"+"grype.txt trivy.txt snyk.txt"
		os.system(str3)
		file = open('exclusiveCVEs','w')
		my_output6 = out(str3)
		file.write(""+my_output6)  
		file.close()
		print("\n")
		print("The Count of CVE in exclusiveCVEs.txt is:")
		str9="python3 cveCounter2.py"
		os.system(str9)
		print("\n")
		print("Hey the list of exclusive CVE is written to file exclusiveCVEs.txt")
		print("Good Bye")
		print("\n")
	else:
		quit()	
	
elif sce==2:

	em=str(input("Enter Name of image:"))
	
	str2="grype "+em
	str3="trivy image "+em
	str4="snyk container test "+em+ " --json"
	str5="./clair_scan --ip=192.168.174.132 "+em
	
	cmd = "docker rm clair ; docker rm db"
	d = os.popen("docker stop clair ; docker stop db; docker rm clair ;  docker rm db ; docker run -p 5432:5432 -d --name db arminc/clair-db:latest ; docker run -p 6060:6060 --link db:postgres -d --name clair arminc/clair-local-scan:latest" )
	dd=d.read()
	#print(dd)
	
	
	
	os.system(str2)	#grype
	file = open('grype.txt','w')
	strA='grype ' +em
	my_output = out(str2)
	file.write(""+my_output)  
	file.close()
	
	os.system(str3)	#trivy
	strB ='trivy image -i '+em
	file = open('trivy.txt','w')
	my_output1 = out(str3)
	file.write(""+my_output1)  
	file.close()
	
	os.system(str4)	#snyk
	file = open('snyk.txt','w')
	my_output3 = out(str4)
	file.write(""+my_output3)  
	file.close()
	
	os.system(str5)	#clair
	file = open('clair.txt','w')
	my_output5 = out(str5)
	file.write(""+my_output5)  
	file.close()
	
	view=str(input("Do you want list of Exclusive CVEs(y/n):"))
	if view=="y":
		str3="python3 cve2.py /"+"grype.txt clair.txt snyk.txt trivy.txt"
		os.system(str3)
		file = open('exclusiveCVEs','w')
		my_output6 = out(str3)
		file.write(""+my_output6)  
		file.close()
		print("\n")
		print("The Count of CVE in exclusiveCVEs.txt is:")
		str9="python3 cveCounter2.py"
		os.system(str9)
		print("\n")
		print("Hey the list of exclusive CVE is written to file exclusiveCVEs.txt")
		print("Good Bye")
		print("\n")
	else:
		quit()	
		
elif sce==3:
	ask=str(input("Put name of text file(example - grype.txt clair.txt snyk.txt trivy.txt:\n"))
	str3="python3 cve2.py "+ask
	os.system(str3)
	file = open('exclusiveCVEs','w')
	my_output6 = out(str3)
	file.write(""+my_output6)  
	file.close()
	print("\n")
	print("Hey the list of exclusive CVE is written to file exclusiveCVEs.txt")
	print("Good Bye")
	print("\n")
		
elif sce==4:
	ask=str(input("Name of file(only one argument supported)\n"))
	str4="python3 cveCounter.py "+ask
	os.system(str4)
	print("\n")
	
elif sce==5:
	ask=str(input("Put name of two file:\n"))
	str4="python3 cve.py "+ask
	os.system(str4)
	print("\n")
	
elif sce==9:
	quit()



	
		                   
                    
                    
