from flask import Flask, request, render_template
from datetime import datetime
import json

app = Flask(__name__)


@app.route("/chat")
def display_chat():
    return render_template("form.html")


@app.route("/")
def index_page():
    return "Добро пожаловать в чат!"


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}


@app.route("/send_message")
def send_message():
    sender = request.args["name"]
    text = request.args["text"]
    add_message(sender, text)
    return "OK"


def load_chat():
    with open("chat.json", "r") as json_file:


all_messages = []


def print_all_messages():
    for message in all_messages:
        name = message["sender"]
        text = message["text"]
        time = message["time"]
        print(f"[{name}] : {text} / {time}")


def add_message(sender, text):
    new_message = {
        "sender": sender,
        "text": text,
        "time": datetime.now().strftime("%H:%M")
    }
    all_messages.append(new_message)


print_all_messages()

app.run()