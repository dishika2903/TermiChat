import socket
import threading
from datetime import datetime

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode('utf-8'))
        except:
            pass

def handle_client(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8', errors='ignore')
            if message:
                timestamp = datetime.now().strftime("[%H:%M:%S]")
                user_index = clients.index(client)
                user = usernames[user_index]
                formatted = f"{timestamp} {user}: {message}"
                print(formatted)

                with open("chat_log.txt", "a", encoding="utf-8") as f:
                    f.write(formatted + "\n")

                broadcast(formatted)
        except:
            if client in clients:
                index = clients.index(client)
                user = usernames[index]
                leave_msg = f"{user} has left the chat"
                print(leave_msg)
                broadcast(leave_msg)
                clients.remove(client)
                usernames.remove(user)
                client.close()
            break

def receive_connections():
    print("Server is running and listening...")
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- Chat started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")

    while True:
        client, addr = server.accept()
        print(f"Connected with {str(addr)}")

        client.send('USERNAME'.encode('utf-8'))
        username = client.recv(2048).decode('utf-8', errors='ignore')
        usernames.append(username)
        clients.append(client)

        join_msg = f"{username} has joined the chat"
        print(join_msg)
        broadcast(join_msg)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

receive_connections()
