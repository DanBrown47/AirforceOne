'''
========================
SSH Automation

The script intends to replace latest build over to a server 
Author Danwand NS | admin@danwand.me

01 Jul 2021
========================
This code is created strictly over the handovered files by Vishnu053
The code does nothing otherthan how the Shell script was intended to do

'''

import os #Executing os commands directly
class main():
    def runUpdate(server_name, server_ip, pem_file_name):
        whoishe = (str(server_name)+"@"+str(server_ip))
        '''
        The core function of the script
        '''
        print("Updating the server "+ str(server_ip)+" with new build\n")
        print("Taking backup of the current build\n")
        # Take a backup of the current build
        os.system(f"ssh -i {pem_file_name} -t {whoishe} 'sudo zip -r client_bkp.zip /srv/client-folder/www'")
        print("backedup to /srv/client-folder/www\n")
        # Copy the new build files
        os.system(f"scp -r -i {pem_file_name} client_build.zip/ {whoishe}:~/")
        # Stopping nginx in server and replace the files
        os.system(f"ssh -i {pem_file_name} -t {whoishe} 'sudo systemctl stop nginx.service'")
        os.system(f"ssh -i {pem_file_name} -t {whoishe} 'sudo unzip ~/client_build.zip -d /srv/client-folder/www'")
        # Start nginx
        os.system(f"ssh -i {pem_file_name} -t {whoishe} 'sudo systemctl start nginx.service'")
