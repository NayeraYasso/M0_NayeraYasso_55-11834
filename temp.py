import socket
import select
import sys
    # Initiate server socket with the TCP connection
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Binding the server socket with the localhost as IP and port number
host = '127.0.0.1' #'192.168.1.24'
port = 5615
server_socket.bind((host, port))
    # Make the socket listen on this port
server_socket.listen(4)
print('Server is Listening')
while True:
        # Accept a client connection
        client_socket, addr = server_socket.accept()
        print('Connected by', addr)

        while True:
            # Receive data from the client
            message = client_socket.recv(1024)
            if not message:
                break  # No more data from client

            message = message.decode('utf-8')
            message_capitalized = message.upper()

            # Send the capitalized message back to the client
            client_socket.send(bytes(message_capitalized, 'utf-8'))

            if message_capitalized == 'CLOSE SOCKET':
                client_socket.close()
                break