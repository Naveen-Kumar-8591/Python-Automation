import paramiko

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
k = paramiko.RSAKey.from_private_key_file(r'C:\Users\DELL\Desktop\1.pem')#Dont tell this line in interviews
client.connect('ec2-3-86-146-51.compute-1.amazonaws.com', port=22, username='ec2-user', password=None, pkey=k)#tell hostname,username, password, portno
stdin, stdout, stderr = client.exec_command('ls -l')

for line in stdout:
    print(line)

client.close()
