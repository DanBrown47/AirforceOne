'''
========================
SSH Automation

The script intends to replace latest build over to a server 
Author Danwand NS | admin@danwand.me

14 Jul 2021
========================
'''
from core.backup import main

if __name__ == '__main__':
    
    # Should add dot env too now hard coding
    
    server_name = input("Enter username of server eg: Ubuntu")
    server_ip = input("Enter IP address of the server")
    pem_file_name = input("pem file name")

    main.runUpdate(server_name,server_ip,pem_file_name)






