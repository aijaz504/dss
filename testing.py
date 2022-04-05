from subprocess import PIPE, run

file = open('geek.txt','w')

def out(command):
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)
    return result.stdout

my_output = out("ls")

var = "mumbai"
print(var)
file.write(""+my_output)
file.close()


