import socket

dank = socket.getfqdn()
host_ip = socket.gethostbyname(dank) 
print(host_ip)
UDP_IP = host_ip#"192.168.1.46"
UDP_PORT = 27015
print(UDP_PORT)
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data