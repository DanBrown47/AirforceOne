import sys
from dotenv import dotenv_values
'''
========================
SSH Automation

The script intends to replace latest build over to a server 
Author Danwand NS | admin@danwand.me

14 Jul 2021
========================
'''
def check_env():
    # Load
    env = dotenv_values(".env")
    server_ip, server_name, pem_file_name = env["SERVER_IP"], env["SERVER_USER"], env["SERVER_PEM_LOCATION"]



from core.backup import main

if __name__ == '__main__':
    check_env()
    sys.exit(1)
    # Should add dot env too now hard coding
    
    server_name = input("Enter username of server eg: ubuntu")
    server_ip = input("Enter IP address of the server")
    pem_file_name = input("pem file name")

    main.runUpdate(server_name,server_ip,pem_file_name)






