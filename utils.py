import json
import os

PROFILE_FILE = "data/user_profile.json"
CHAT_FILE = "data/chat_history.json"


def save_profile(data):
    with open(PROFILE_FILE, "w") as f:
        json.dump(data, f)


def load_profile():
    if os.path.exists(PROFILE_FILE):
        with open(PROFILE_FILE) as f:
            return json.load(f)
    return {}


def save_chat(chat):
    with open(CHAT_FILE, "w") as f:
        json.dump(chat, f)


def load_chat():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE) as f:
            return json.load(f)
    return []
