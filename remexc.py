import subprocess
from subprocess import PIPE
import os
user = raw_input("Target User:")
target_ip = raw_input("IP address of remote machine:")
port = raw_input("Port number:")
password = raw_input("Enter the password:")
cmd = "python /home/{}/Downloads/DDosTest.py --ip:{} --port:{} --time:10".format(target_ip,port,user)
#p = subprocess.Popen("pscp.exe C://Users//sarak//Desktop//project//DDosTest.py {}@{}:/home/sarak/Downloads/".format(user,target_ip))
#p = subprocess.Popen("putty.exe -pw {} {}@{}".format(password,user,target_ip).split(' '),stdin = PIPE,stdout = PIPE)
#p.stdin.write(cmd)
#print(p.stdout)
#p.wait()
#sts = os.waitpid(p.pid,0)(
p = subprocess.Popen("plink.exe -pw {} {}@{}".format(password,user,target_ip).split(' '),shell = False)

