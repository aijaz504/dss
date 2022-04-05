import os
import sys
import re

# usage example for windows : cve.py \Anchore\A_mongo.txt \Clair\C_mongo.txt
# usage example for linux : python3 cve.py /Anchore/A_mongo.txt /Trivy/T_mongo.txt

if len(sys.argv)<=1:
	print("enter correct file locations(2)")
	exit(1)

f = os.getcwd()+'/'+sys.argv[1]
g = os.getcwd()+'/'+sys.argv[2]
#R=open("result.txt","w")

#f = os.getcwd()+"\\Anchore\\A_mongo.txt"
#g = os.getcwd()+"\\Clair\\C_mongo.txt"
#print(f)
#print(os.getcwd())
A=open(f,encoding='utf8')
B=open(g,encoding='utf8')
linesA=A.readlines()
linesB=B.readlines()
cveA=[]
cveB=[]
cveCommon=[]
for m in linesA:
    #print(m)
    try:
        i=m.index("CVE-")
        c=m[i:i + 17].strip()
        if c not in cveA:
            cveA.append("CVE"+re.sub("[^\d\-]", "",c))
    except:
        continue
for m in linesB:
    try:
        i = m.index("CVE-")
        c = m[i:i + 17].strip()
        if c not in cveB:
            cveB.append("CVE"+re.sub("[^\d\-]", "",c))
    except:
        continue
cveExclusiveA=[]
cveExclusiveB=[]
for x in range(len(cveA)):
    if cveA[x] in cveB:
        if cveA[x] not in cveCommon:
            cveCommon.append(cveA[x])
    else:
        if cveA[x] not in cveExclusiveA:
            cveExclusiveA.append(cveA[x])
for x in range(len(cveB)):
    if cveB[x] not in cveA:
        if cveB[x] not in cveExclusiveB:
            cveExclusiveB.append(cveB[x])
#stacked view
'''
print("\nTotal CVE in A")
print('─' * 20)
print(*cveA)
print("\nTotal CVE in B")
print('─' * 20)
print(*cveB)
'''

print("\nCommon cve")
print('─' * 20)
print(*cveCommon)
print("\nCVE exclusive to A(First argument you provided)")
print('─' * 20)
print(*cveExclusiveA)
print("\nCVE exclusive to B(Second argument you provided")
print('─' * 20)
print(*cveExclusiveB)


#list view

'''
print("\ncve of A\n",*cveA,sep='\n')
print("\ncve of B\n",*cveB,sep='\n')
print("\nCommon cve\n",*cveCommon,sep='\n')
print("\ncve exclusive to A\n",*cveExclusiveA,sep='\n')
print("\ncve exclusive to B\n",*cveExclusiveB,sep='\n')

R.write("cve of A\n\n")
for x in cveA:
    R.write(x+"\n")
R.write("\ncve of B\n\n")
for x in cveB:
    R.write(x+"\n")
R.write("\ncve common in A and B\n\n")
for x in cveCommon:
    R.write(x+"\n")
R.write("\ncve exclusive to A\n\n")
for x in cveExclusiveA:
    R.write(x+"\n")
R.write("\ncve exclusive to B\n\n")
for x in cveExclusiveB:
    R.write(x+"\n")
'''

A.close()
B.close()
#R.close()
