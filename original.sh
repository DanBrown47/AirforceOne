#!/bin/bash

runUpdate() {
    cd updateFiles
    # Take a backup of the current build
    ssh -i the_ssh_file.pem -t $1 'sudo zip -r client_bkp.zip /srv/client-folder/www'
    # Copy the new build files
    scp -r -i the_ssh_file.pem client_build.zip/ $1:~/
    # Stopping nginx in server and replace the files
    ssh -i the_ssh_file.pem -t $1 'sudo systemctl stop nginx.service'
    ssh -i the_ssh_file.pem -t $1 'sudo unzip ~/client_build.zip -d /srv/client-folder/www'
    # Start nginx
    ssh -i the_ssh_file.pem -t $1 'sudo systemctl start nginx.service'
    cd ..

}
#Call the methods
runUpdate "ubuntu@server1_ip"
runUpdate "ubuntu@server2_ip"