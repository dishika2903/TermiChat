import socket
import threading
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

def log_message(sender, message):
    with open("chatlog.txt", "a") as f:
        f.write(f"[{datetime.now().strftime('%H:%M')}] {sender}: {message}\n")

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 5000))
server_socket.listen()

print(f"{Fore.GREEN}🟢 Server started. Waiting for connection...")

client_socket, address = server_socket.accept()
username = client_socket.recv(1024).decode()
print(f"{Fore.MAGENTA}[{datetime.now().strftime('%H:%M')}] {username} connected from {address}")

with open("chatlog.txt", "a") as f:
    f.write(f"\n--- Chat started at {datetime.now().strftime('%H:%M')} with {username} ---\n")

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            if not message or message.lower() == "exit":
                print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M')}] {username} disconnected.")
                break
            timestamp = datetime.now().strftime('%H:%M')
            print(f"{Fore.CYAN}[{timestamp}] {username}: {message}")
            log_message(username, message)
        except:
            break

def send_messages():
    while True:
        try:
            message = input(f"{Fore.GREEN}Server: ").strip()
            if not message:
                continue
            client_socket.send(message.encode())
            log_message("Server", message)
            if message.lower() == "exit":
                print(f"{Fore.RED}🔌 Server ended the chat.")
                break
        except:
            print(f"{Fore.RED}❌ Failed to send message.")
            break

recv_thread = threading.Thread(target=receive_messages, daemon=True)
send_thread = threading.Thread(target=send_messages)

recv_thread.start()
send_thread.start()

send_thread.join()
client_socket.close()
server_socket.close()
