import socket
import threading

# Trying to select a port that's not usually used
PORT = 5050

SERVER = socket.gethostbyname(socket.gethostname())     # fetch the local ip address of the system
ADDR = (SERVER, PORT)       # Address of a system is determined by the ip address and the port number
HEADER = 64                 # Size of each message
FORMAT = 'utf-8'            # format of each message to be encoded into
DISCONNECT_MESSAGE = '!DISCONNECT'      # disconnect command

# Creating a socket...
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected...")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            print(f"[{addr}] {msg}")
            conn.send("{ADDR}: {msg}".encode(FORMAT))
 
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # multi threading is used to handle numerous clients simultaneously
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] Server is starting...")
start()