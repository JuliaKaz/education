from flask import Flask, request, render_template
import time

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


t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

all_messages = [{
    "sender": "Julia",
    "text": "Hello",
    "time": current_time
}]


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
        "time": current_time
    }
    all_messages.append(new_message)


print_all_messages()

app.run()