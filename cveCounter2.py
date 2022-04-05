
with open('exclusiveCVEs', 'r') as file:
    data = file.read().replace('\n', '')
    
with open('exclusiveCVEs', 'r') as file:
    data = file.read().rstrip()
#print("String coverted to list :",data.split())     

print(data.count("CVE-"))




    
    
    

