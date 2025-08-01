import socket
import threading
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

HOST = 'localhost'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
usernames = []

# Add chat started message once at startup
def log_chat_start():
    start_time = datetime.now().strftime("=======Chat started at %Y-%m-%d %H:%M:%S=======")
    with open("chat_log.txt", "a") as file:
        file.write(start_time + "\n")
    print(Fore.CYAN + start_time)

def broadcast(message, _client=None):
    for client in clients:
        if client != _client:
            try:
                client.send(message.encode())
            except:
                client.close()

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message.lower() == "/exit":
                remove_client(client)
                break
            timestamp = datetime.now().strftime("[%H:%M:%S]")
            index = clients.index(client)
            username = usernames[index]
            full_message = f"{timestamp} {username}: {message}"
            log_chat(full_message)
            broadcast(full_message, client)
        except:
            remove_client(client)
            break

def receive_connections():
    print(Fore.GREEN + f"Server started on {HOST}:{PORT}..." + Style.RESET_ALL)
    log_chat_start()  # Call it once when server starts
    while True:
        client, addr = server.accept()
        print(Fore.YELLOW + f"New connection from {addr}" + Style.RESET_ALL)
        client.send("USERNAME".encode())
        username = client.recv(1024).decode()
        usernames.append(username)
        clients.append(client)

        join_message = f"{username} has joined the chat."
        log_chat(Fore.CYAN + join_message)
        broadcast(join_message, client)

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        username = usernames[index]
        clients.remove(client)
        usernames.remove(username)
        client.close()
        leave_message = f"{username} has left the chat."
        log_chat(Fore.MAGENTA + leave_message)
        broadcast(leave_message)

def log_chat(message):
    plain_text = Style.RESET_ALL.join(message.split(Style.RESET_ALL))  
    with open("chat_log.txt", "a") as file:
        file.write(strip_ansi(plain_text) + "\n")
    print(message)

def strip_ansi(text):
    import re
    ansi_escape = re.compile(r'\x1B[@-_][0-?]*[ -/]*[@-~]')
    return ansi_escape.sub('', text)

receive_connections()
