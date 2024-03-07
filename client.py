import threading
import socket
import ssl

nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ssl_context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE
ssl_client = ssl_context.wrap_socket(client, server_hostname='127.0.0.1')

ssl_client.connect(('127.0.0.1', 55555))

def receive():
    while True:
        try:
            message = ssl_client.recv(1024).decode('ascii')
            if message == 'NICK':
                ssl_client.send(nickname.encode('ascii'))
            else:
                print(message)
        except ConnectionResetError:
            print("An error occurred")
            ssl_client.close()
            break

def write():
    while True:
        message = f'{nickname}: {input()}'
        ssl_client.send(message.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
