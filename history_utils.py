import json
import os

FILE_NAME = "chat_history.json"


def save_history(messages):

    with open(FILE_NAME, "w") as f:
        json.dump(messages, f)


def load_history():

    if not os.path.exists(FILE_NAME):
        return []

    with open(FILE_NAME, "r") as f:
        return json.load(f)
