import threading
import socket
import ssl

# Create address for server
host = '127.0.0.1'  # localhost
port = 55555

# Using for receive all connect from client
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Initialize threads for each client separately
clients = []
nicknames = []

# Send mesage to all clients in list
def broadcast(message):
    for client in clients:
        client.send(message)

# Handles receiving and responding to 
# messages from a specific client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except ConnectionResetError:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('ascii'))
            nicknames.remove(nickname)
            break

# Using for receive,accept and handle all connect from cilents
def receive():
    while True:
        client_socket, address = server.accept()
        print(f"Connected with {str(address)}")
        
        # SSL/TLS used to protect connect
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(certfile="server.pem", keyfile="server.key")
        ssl_client_socket = ssl_context.wrap_socket(client_socket, server_side=True)

        ssl_client_socket.send('NICK'.encode('ascii'))
        nickname = ssl_client_socket.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(ssl_client_socket)

        print(f'Nickname of client is {nickname}!')
        broadcast(f'{nickname} joined the chat'.encode('ascii'))
        ssl_client_socket.send('Connected to server'.encode('ascii'))

        thread = threading.Thread(target=handle, args=(ssl_client_socket,))
        thread.start()

# Print status of server
print("Server is listening...")
receive()
