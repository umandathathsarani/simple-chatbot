# Customer Support Chatbot

A full-stack, rule-based customer support web application. This project provides an interactive, modern conversational interface that parses dynamic JSON rules to intelligently match user intent and instantly answer queries.

## 🚀 Features

* **Intelligent Intent Matching:** Utilizes Python's Regular Expressions (`re` module) to understand varied user inputs and keyword variations.
* **Separation of Concerns:** Bot responses and rules are externalized in a `responses.json` data store, allowing easy content updates without altering core application logic.
* **Modern Web Interface:** A responsive, WhatsApp-style graphical user interface built with HTML5 and custom CSS Flexbox.
* **Quick Reply Suggestions:** Interactive UI chips that allow users to send common queries with a single click.
* **Automated Audit Logging:** Silently tracks and logs all conversation histories with timestamps to a local backend file for managerial review.

## 💻 Tech Stack

* **Backend:** Python 3, Flask
* **Frontend:** Vanilla JavaScript, HTML5, CSS3
* **Data Storage:** JSON (Rule Configuration), TXT (Audit Logs)

## 📂 Project Structure

```text
├── static/
│   └── favicon.ico          # Browser tab icon
├── templates/
│   └── index.html           # Frontend web interface
├── app.py                   # Core Flask server and regex logic
├── responses.json           # Editable intent rules and fallback arrays
├── chat_log.txt             # Auto-generated conversation history
└── README.md                # Project documentation
```

## 🛠️ Installation & Setup

1. Clone the repository:
```
git clone [https://github.com/umandathathsarani/simple-chatbot.git](https://github.com/umandathathsarani/simple-chatbot.git)

cd simple-chatbot
``` 

2. Install dependencies:
Ensure you have Python installed, then install the Flask web framework:
```
pip install flask
```

3. Run the application:
```
python app.py
```

4. Access the interface:
Open a web browser and navigate to the link provided in the terminal.

## 📄 License
This project is proprietary. All rights reserved. No unauthorized copying, distribution, or modification is permitted.