import socket
import threading
from colorama import Fore, Style, init

init(autoreset=True)

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

username = input("Enter your username: ")

def format_message(message):
    if any(keyword in message for keyword in ["has joined the chat", "has left the chat"]):
        return Fore.YELLOW + Style.BRIGHT + message

    try:
        timestamp, content = message.split(" ", 1)
        user, msg = content.split(":", 1)
        if user.strip() == username:
            return (Fore.WHITE + Style.DIM + timestamp + " " +
                    Fore.GREEN + Style.BRIGHT + user.strip() + ":" +
                    Fore.GREEN + msg)
        else:
            return (Fore.WHITE + Style.DIM + timestamp + " " +
                    Fore.CYAN + user.strip() + ":" +
                    Fore.CYAN + msg)
    except:
        return message

def receive_messages():
    while True:
        try:
            message = client.recv(2048).decode('utf-8', errors='ignore')
            if message == 'USERNAME':
                client.send(username.encode('utf-8'))
            else:
                print(format_message(message))
        except:
            print(Fore.RED + Style.BRIGHT + "Disconnected from server.")
            client.close()
            break

def send_messages():
    while True:
        message = input()
        if message.lower() == '/exit':
            client.close()
            break
        try:
            client.send(message.encode('utf-8'))
        except:
            break

print(f"Welcome, {username}! Type your message and press Enter to send. Type '/exit' to leave.\n")

recv_thread = threading.Thread(target=receive_messages)
recv_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
