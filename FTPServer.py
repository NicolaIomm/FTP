import socket
from FTPlib import *

def getIPLAN():
    address = socket.getfqdn()
    l = address.split(".")
    return l[3]+"."+l[2]+"."+l[1]+"."+l[0]

def serve_client(connection, address):
    msg = "\
           +-----------------------------------------------+ \n\
           |  Welcome to "+HOST+" FTPServer\t   | \n\
           +-----------------------------------------------+ "
    connection.sendall(msg.encode())
    while (True):
        msg = connection.recv(1024).decode()
        if (msg == "QUIT"):
            break
        else:
            print("Received: "+msg)
            response = "I can't understand. Repeat pls."
            connection.sendall(response.encode())
    print("[DEBUG] QUIT command received.")
        
HOST = getIPLAN()
PORT = 3000    

if __name__ == "__main__":

    server_address = (HOST, PORT)
    
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.bind(server_address)
    server_sock.listen(3)

    print("[DEBUG] Server started on "+ HOST +":"+str(PORT))

    while (True):
        try:
            (connection, address) = server_sock.accept()
            serve_client(connection, address)
            connection.close()
        except KeyboardInterrupt:
            break

    print("[DEBUG] Server is closing.. BYE")
