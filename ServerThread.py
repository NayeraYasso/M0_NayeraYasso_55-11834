import socket
import threading

def threaded(conn, addr):
 while True :
     #print(F"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
     message = conn.recv(1024)
     if not message:
         break 
     message = message.decode('utf-8')
     message_capitalized = message.upper()
     conn.send(bytes(message_capitalized, 'utf-8'))
     if message_capitalized == 'CLOSE SOCKET':
         conn.close()
         break
     
def main():
    PORT = 5604   
    print(" Server is starting...")
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1',PORT))
    print("socket binded to port", PORT)
    server_socket.listen(3)
    while True:
        if(threading.active_count() - 1-6 <3):
            conn, addr = server_socket.accept()
            print('connected to:', addr[0], ':', addr[1]) 
       #print(F"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
            threading.Thread(target=threaded, args=(conn,addr)).start()
            print(F"[ACTIVE CONNECTIONS] {threading.active_count() - 1-6}")
    
    
if __name__ == "__main__":
 main()
