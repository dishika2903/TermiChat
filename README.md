TermiChat
TermiChat is a terminal-based chat application built in Python using socket programming and multithreading. It allows real-time communication between multiple users with color-coded messages, timestamps, usernames, chat logging, message clearing, private messaging, and emoji support — all in your terminal!

🚀 Features
✅ Real-time multi-client messaging
🧵 Multithreaded server-client architecture
⏰ Timestamps for all messages
🎨 Colored terminal output using Colorama
📁 Server-side chat logs saved with timestamps
👤 Usernames displayed with messages
🔌 Clean exit with exit command
🧹 Message clearing command /clear to tidy your chat
🤫 Private messaging command /w username message for one-on-one chats
😄 Emoji support for expressive conversations
⚠️ Error handling and safe disconnection

📁 Project Structure
TermiChat/
├── server.py          # Server-side code to handle multiple clients and messaging
├── client.py          # Client-side code to send/receive messages
├── chatlog.txt        # Server-side log file for chat history
└── README.md          # Project documentation

🛠️ How to Run
Clone the repository
Install dependencies
Make sure you have Python installed. Then install the required package:
pip install colorama
Run the server
Open a terminal and run:
python server.py
Run the client(s)
Open one or more terminals and run:
python client.py
Start chatting!
Enter your username and start chatting in real-time. Use commands like /clear to clear your messages and /w username message to send private messages.

💻 Technologies Used
🐍 Python 3
🔌 Socket Programming
🔁 Multithreading
🎨 Colorama (for terminal coloring)

🔮 Future Improvements
✍️ Add "typing..." indicator
🪟 Build a GUI interface using Tkinter or PyQt
🌐 Create a full-stack version with database and frontend
👥 Enhance online user tracking and status commands

📄 License
This project is licensed under the MIT License.
