import subprocess
import os
import platform
import getpass
try:
    user = getpass.getuser()
    remuser = raw_input("Target User:")
    target_ip = raw_input("IP address of remote machine:")
    filename = raw_input("Enter ur file name:")
    cmd = "python DDosTest.py"
    if platform.system() == 'Windows':
        #p = subprocess.Popen("pscp.exe C://Users//{}//Desktop//project//{} {}@{}:/home/{}/Downloads/".format(user,filename,remuser,target_ip,remuser))
        p = subprocess.Popen("pscp.exe C://Users//{}//Desktop//project//{} {}@{}:/home/{}/".format(user,filename,remuser,target_ip,remuser))
    elif platform.system() == 'Linux':
        p = subprocess.Popen("scp /home/{}/Downloads/{} {}@{}:C:/user/{}/Downloads/".format(user,filename,remuser,target_ip,remuser))
#p = subprocess.Popen("pscp.exe -pw @rk21"+ user+"@"+target_ip+":/home/"+user+"/Downloads/ 'C://Users//sarak//Desktop//project//DDosTest.py'")
#p = subprocess.Popen(["plink.exe",user+"@"+target_ip,cmd])
#sts = os.waitpid(p.pid,0)
    print(p.pid)
except KeyboardInterrupt:
    print("You interrupted it")
