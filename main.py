#/user/bin/env/pythoon

import subprocess
subprocess.run("clear",shell=True)   

subprocess.run("cd ~",shell=True)   

# update
subprocess.run("apt update -y",shell=True)   
subprocess.run("apt upgrade -y",shell=True) 

# add path
subprocess.run("cp 'menu/menu' '/bin/'",shell=True)
subprocess.run("chmod +x /bin/menu",shell=True)

#install ssh
subprocess.run("bash tunnel.sh",shell=True)

#install open VPN
subprocess.run("bash open_vpn",shell=True)

exit()
