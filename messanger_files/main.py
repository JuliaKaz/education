from flask import Flask
import time

app = Flask(__name__)


@app.route("/")
def index_page():
    return "Добро пожаловать в чат!"


@app.route("/get_messages")
def get_messages():
    return {"messages": all_messages}



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