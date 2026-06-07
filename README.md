# 🤖 Customer Support Chatbot

> A full-stack, rule-based conversational AI agent and customer support web application designed to handle automated user queries instantly, efficiently, and reliably.

## 🎓 Academic Context

**Program:** Bachelor of Science Honours in Information Technology  
**Specialization:** Artificial Intelligence  

This repository represents a practical application of core software engineering principles, data parsing, and foundational natural language processing (NLP) concepts through Regular Expressions.

---

## 🌟 Project Overview

Modern businesses require rapid response times for standard customer inquiries. This project bridges the gap between static FAQ pages and live human agents by providing an interactive, intelligent chatbot interface. 

Instead of hardcoding responses into the application logic, this system utilizes a decoupled architecture. The conversational rules and bot responses are externalized in a dynamic JSON data store. The Flask backend acts as the brain, intercepting user messages from the frontend, parsing them using Regular Expression (Regex) intent matching, and serving the appropriate automated response based on the dataset.

---

## 🚀 Key Features

* **Intelligent Intent Matching:** Moves beyond basic exact-string matching by utilizing Python's `re` module. The bot understands varied user inputs, synonyms, and keyword variations (e.g., matching "deliver", "ship", or "track" to the same shipping intent).

* **Decoupled Data Architecture:** Bot responses, intents, and fallback arrays are isolated in a `responses.json` file. This allows non-technical team members to update the bot's dialogue without ever touching or risking the core Python logic.

* **Modern Messaging Interface:** A fully responsive, WhatsApp-style graphical user interface built from scratch with HTML5 and custom CSS Flexbox. It features dynamic chat bubbles, scrolling message containers, and a clean aesthetic.

* **Quick-Reply UI Chips:** Interactive suggestion buttons located above the chat input that allow users to instantly send high-frequency queries with a single click, drastically improving user experience and accessibility.

* **Automated Audit Logging:** The server silently tracks and records all user-bot interactions, appending them with precise timestamps to a local `chat_log.txt` file. This is crucial for managerial review, debugging, and identifying areas where the bot's dataset needs expansion.

---

## 💻 Technical Stack

* **Backend Environment:** Python 3
* **Web Framework:** Flask (Routing, JSON parsing, API endpoints)
* **Frontend Languages:** Vanilla JavaScript (Fetch API, DOM manipulation), HTML5, CSS3
* **Data Storage:** JSON (Rule Configuration), TXT (Persistent Audit Logs)
* **Version Control:** Git & GitHub

---

## 📂 System Architecture

```text
simple-chatbot/
├── static/
│   └── favicon.ico          
├── templates/
│   └── index.html           
├── app.py                   
├── responses.json           
├── chat_log.txt             
└── README.md             
```

---

## 🛠️ Installation & Local Setup

1. Clone the repository:
```
git clone [https://github.com/umandathathsarani/simple-chatbot.git](https://github.com/umandathathsarani/simple-chatbot.git)
cd simple-chatbot
``` 

2. Configure the Python environment:
Ensure you have Python 3.x installed on your machine. Install the required Flask web framework using pip:
```
pip install flask
```

3. Initialize the server:
Start the Flask development server from your terminal:
```
python app.py
```

4. Access the web interface:
Once the server is active, open any modern web browser and navigate to the local host address provided in the terminal

---

## 📄 License
Copyright (c) 2026 Mummullage Binuri Umanda Thathsarani

This project is proprietary. All rights reserved. No unauthorized copying, reproduction, distribution, or modification of this software, its source code, or its design assets is permitted. This repository is published strictly for academic demonstration and professional portfolio purposes.