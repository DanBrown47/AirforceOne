'''
========================
SSH Automation

The script intends to replace latest build over to a server 
Author Danwand NS | admin@danwand.me
14 Jul 2021
========================
'''

import os #Executign os commands directly
def runUpdate(client, server_ip, pem_file_name):
    whoishe = (str(client)+"@"+str(server_ip))
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
if __name__ == '__main__':
    # Should add dot env too now hard coding
    
    runUpdate("ubuntu","127.0.0.1","pemfile")






