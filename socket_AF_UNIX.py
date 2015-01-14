import socket
import sys
import os

class Server():
    def __init__(server_address ='./uds_socket'): 
        self.server_address = server_address
    # Make sure the socket does not already exist
    def start():
        try:
        os.unlink(server_address)
        except OSError:
            if os.path.exists(server_address):
                raise
        # Create a UDS socket
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # Bind the socket to the port
        print >>sys.stderr, 'starting up on %s' % server_address
        sock.bind(server_address)
        # Listen for incoming connections
        sock.listen(1)

    def communicate():
        while True:
            # Wait for a connection
            print >>sys.stderr, 'waiting for a connection'
            connection, client_address = sock.accept()
            try:
                print >>sys.stderr, 'connection from', client_address
                # Receive the data in small chunks and retransmit it
                while True:
                    data = connection.recv(16)
                    print >>sys.stderr, 'received "%s"' % data
                    if data:
                        print >>sys.stderr, 'sending data back to the client'
                        connection.sendall(data)
                    else:
                        print >>sys.stderr, 'no more data from', client_address
                        break
            except e:
	        print str(e)             
            finally:
                # Clean up the connection
                connection.close()


class Client():
    def __init__(server_address = './uds_socket'):
	self.server_address = server_address

    def connect():	
	# Create a UDS socket
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	# Connect the socket to the port where the server is listening
	server_address = './uds_socket'
	print >>sys.stderr, 'connecting to %s' % server_address
	try:
    	    sock.connect(server_address)
	except socket.error, msg:
    	    print >>sys.stderr, msg
    	    sys.exit(1)
    
    def communicate('./uds_socket'n):
	try:
    	    # Send data
    	    message = 'This is the message.  It will be repeated.'
    	    print >>sys.stderr, 'sending "%s"' % message
    	    sock.sendall(message)
    	    amount_received = 0
     	    amount_expected = len(message)
    	    while amount_received < amount_expected:
            	data = sock.recv(16)
        	amount_received += len(data)
        	print >>sys.stderr, 'received "%s"' % data
	finally:
    	    print >>sys.stderr, 'closing socket'
    	    sock.close()
        
