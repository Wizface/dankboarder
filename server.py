
import socket
import time
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 27015  # Port to listen on (non-privileged ports are > 1023)


def main():

    def get_Host_name_IP(): 
        try: 
            host_name = socket.gethostname() 
            host_ip = socket.gethostbyname(host_name) 
            print("Hostname :  ",host_name) 
            print("IP : ",host_ip) 
        except: 
            print("Unable to get Hostname and IP") 
  
    # Driver code 
    get_Host_name_IP() #Function call 

    while True:
        #open a file and load the message. then send message on loop
        
        
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            (conn, addr) = s.accept()
            with conn:
                print('User Connected by', addr)
                poss = 90000
                package = str.encode(str(poss))
                #while True:
                data = conn.recv(1024)
                conn.sendall(package)
        #print('-> Username is:', repr(data))
        
        time.sleep(.1)


if __name__ == '__main__':
    main()

			