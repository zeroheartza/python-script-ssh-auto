import paramiko

SSH_ADDRESS = "HOST_IP"
SSH_USERNAME = "USERNAME"
SSH_PASSWORD = "PASSWORD"
directory=""
command=""
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(SSH_ADDRESS, username=SSH_USERNAME, password=SSH_PASSWORD)
while(command.upper()!="EXIT"): 
    command=raw_input(SSH_USERNAME+"@"+SSH_ADDRESS+" # ")
    if(command[0:2]=="cd"):
        if(command[2:]==""):
            directory=""
        else:
            directory+="cd"+command[2:]+"&&"
    stdin, stdout, stderr = client.exec_command(directory+command)
    for line in stdout:
        print(line.strip('\n')) 
client.close()
