import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'

# This is the local IP of my server. Use the ip of your own server... 
SERVER = ''
DISCONNECT_MESSAGE = '!DISCONNECT'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)

    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))
    
while(True):
    mssg = input("Enter your message...")
    send(mssg)

    if mssg == DISCONNECT_MESSAGE :
        print("Disconnected...")
        break
