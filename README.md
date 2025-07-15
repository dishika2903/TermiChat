# 💬 TermiChat - Terminal Chat App using Python

**TermiChat** is a terminal-based chat application built in Python using socket programming and multithreading. It allows real-time communication between two users with color-coded messages, timestamps, usernames, and chat logging — all in your terminal!

---

## 🚀 Features

- ✅ Real-time two-way messaging
- 🧵 Multithreaded server-client architecture
- ⏰ Timestamps for all messages
- 🎨 Colored terminal output using `colorama`
- 📁 Server-side chat logs saved with timestamps
- 👤 Usernames displayed with messages
- 🔌 Clean exit with "exit" command
- ⚠️ Error handling and safe disconnection

---

## 📁 Project Structure

TermiChat/
├── server.py          # Server-side code to handle incoming messages
├── client.py          # Client-side code to send/receive messages
├── chatlog.txt        # Logs all chat history on server-side
└── README.md          # Project documentation

---

## 🛠️ How to Run
1.Clone the Repository

2.Install Dependencies
Make sure you have Python installed.
Then, install colorama:
pip install colorama

3.Run the Server
Open one terminal and run:
python server.py

4.Run the Client
Open another terminal and run:
python client.py

5.Start Chatting!
Enter your username and start chatting between terminals in real-time 🎉

---

## 💻 Technologies Used
-🐍 Python 3
-🔌 Socket Programming
-🔁 Multithreading
-🎨 Colorama (for terminal coloring)

---

## 🔮 Future Improvements
-✍️ Add "typing..." indicator
-😄 Support for emojis
-👥 Enable multiple client connections
-🪟 Build a GUI interface using Tkinter or PyQt
-🌐 Create a full-stack version with database and frontend

---

## 📄 License
This project is licensed under the MIT License.
