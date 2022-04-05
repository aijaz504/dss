import os
import sys
import re

# usage example for windows : cve.py \Anchore\A_mongo.txt \Clair\C_mongo.txt
# usage example for linux : python3 cve.py /Anchore/A_mongo.txt /Trivy/T_mongo.txt

if len(sys.argv)<=1:
	print("enter correct file locations(2)")
	exit(1)

f = os.getcwd()+'/'+sys.argv[1]
#R=open("result.txt","w")

A=open(f,encoding='utf8')

linesA=A.readlines()

cveA=[]


for m in linesA:
    #print(m)
    try:
        i=m.index("CVE-")
        c=m[i:i + 17].strip()
        if c not in cveA:
            cveA.append("CVE"+re.sub("[^\d\-]", "",c))
    except:
        continue
        
#stacked view
#print("\nTotal CVE in A")
#print('─' * 20)
#print(*cveA)
cveA = list(dict.fromkeys(cveA))
#print(cveA)
print("\nTotal count of CVE in A")
print('─' * 30)
print(len(cveA))






A.close()
#R.close()
