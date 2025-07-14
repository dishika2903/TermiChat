import socket
import threading
from datetime import datetime
from colorama import init, Fore

init(autoreset=True)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 5000))

username = input("Enter your username: ").strip()
client.send(username.encode())

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            if not message or message.lower() == "exit":
                print(f"{Fore.YELLOW}[{datetime.now().strftime('%H:%M')}] Server disconnected.")
                break
            timestamp = datetime.now().strftime('%H:%M')
            print(f"{Fore.MAGENTA}[{timestamp}] Server: {message}")
        except:
            break

def send_messages():
    while True:
        message = input(f"{Fore.CYAN}{username}: ").strip()
        if not message:
            continue
        client.send(message.encode())
        if message.lower() == "exit":
            break

receive_thread = threading.Thread(target=receive_messages, daemon=True)
send_thread = threading.Thread(target=send_messages)

receive_thread.start()
send_thread.start()

send_thread.join()
client.close()
