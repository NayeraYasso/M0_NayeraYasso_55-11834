import socket
import select
import sys
#initiate Client socket with the TCP connection
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# binding the client socket with the localhost as ip and port number
port=5615
# try to connect to the server with associated port and id
client_socket.connect(('127.0.0.1',port)) #'127.0.0.1' is the localhost in ipv4␣
#↪format
# open a connection until sending CLOSE SOCKET
while True:
    message=input("enter your message: ")
    client_socket.send(bytes(message,'utf-8'))
    received_message = client_socket.recv(1024)  
    received_messaged = received_message.decode('utf-8')
    print(received_messaged)
    if received_message == 'CLOSE SOCKET': 
        client_socket.close()
        break
    