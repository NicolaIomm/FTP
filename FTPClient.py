import socket
import sys

HOST = sys.argv[1]
PORT = (int)(sys.argv[2])

def go():
    while (True):
        response = sock.recv(1024).decode()
        print("Received: " + response)
        try:
            request = input("Request: ")
            sock.sendall(request.encode())
            if (request == "QUIT"):
                break
        except KeyboardInterrupt:
            break
    QUIT_COMMAND = "QUIT"
    sock.sendall(QUIT_COMMAND.encode())

if __name__ == "__main__":
    if (len(sys.argv) < 3):
        print("Usage: python3 FTPClient.py <server_ip> <port>")
        sys.exit(0)
        
    server_address = (HOST, PORT)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(server_address)

    print("[DEBUG] Client connected to "+HOST+":"+str(PORT)+".")

    go()
    sock.close()
    
    print("[DEBUG] Connection is closing.. BYE")
        
        

            
            
    
    
