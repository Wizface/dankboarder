import socket
import sys

server_address = ('http://dankboarder.ddns.net', 27015)

def main():
    while True:
        # Create a TCP/IP socket
        # Connect the socket to the port where the server is listening
        
        print >>sys.stderr, 'connecting to %s port %s' % server_address


        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect(server_address)

        dank_bever = 2232

        # Send data
        message = 'Here are the co-ords:  ' + str(dank_bever)
        print(type(message))
        print >>sys.stderr, 'sending "%s"' % message
        sock.sendall(message)
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        #while amount_received < amount_expected:
        #    data = sock.recv(16)
        #    amount_received += len(data)
        
        #    print >>sys.stderr, 'received "%s"' % data
if __name__ == '__main__':
    main()


#finally:
#    print >>sys.stderr, 'closing socket'
#    sock.close()