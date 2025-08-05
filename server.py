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

def send_private_message(sender_client, target_username, private_msg):
    if target_username in usernames:
        target_index = usernames.index(target_username)
        target_client = clients[target_index]
        sender_index = clients.index(sender_client)
        sender_username = usernames[sender_index]
        timestamp = datetime.now().strftime("[%H:%M:%S]")

        formatted = f"{timestamp} [PRIVATE] {sender_username} to {target_username}: {private_msg}"

        try:
            target_client.send(formatted.encode('utf-8'))  # Send to recipient
            sender_client.send(formatted.encode('utf-8'))  # Also confirm to sender
        except:
            pass

        # Optional: log private messages
        with open("chat_log.txt", "a", encoding="utf-8") as f:
            f.write(formatted + "\n")

    else:
        sender_client.send(f"User '{target_username}' not found.".encode('utf-8'))

def handle_client(client):
    while True:
        try:
            message = client.recv(2048).decode('utf-8', errors='ignore')
            if message:
                user_index = clients.index(client)
                user = usernames[user_index]

                if message.startswith('/w '):
                    try:
                        parts = message.split(' ', 2)
                        target_user = parts[1]
                        private_msg = parts[2]
                        send_private_message(client, target_user, private_msg)
                    except IndexError:
                        client.send("Invalid format. Use /w username message".encode('utf-8'))
                    continue

                timestamp = datetime.now().strftime("[%H:%M:%S]")
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
