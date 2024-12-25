from flask import Flask, render_template, request, jsonify
import json
import os
from pynput.keyboard import Controller, Key

app = Flask(__name__)
keyboard = Controller()
CONFIG_FILE = "button_config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f"{CONFIG_FILE} does not exist.")
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)

def press_keys(hotkey):
    keys = hotkey.split("+")
    key_objects = []
    for key in keys:
        if hasattr(Key, key):
            key_objects.append(getattr(Key, key))
        else:
            key_objects.append(key)
    for key in key_objects[:-1]:
        keyboard.press(key)
    keyboard.press(key_objects[-1])
    keyboard.release(key_objects[-1])
    for key in reversed(key_objects[:-1]):
        keyboard.release(key)

@app.route("/")
def index():
    config = load_config()
    return render_template("index.html", buttons=config)

@app.route("/press", methods=["POST"])
def press():
    data = request.json
    hotkey = data.get("hotkey")
    if not hotkey:
        return jsonify({"status": "error", "message": "No hotkey provided"}), 400

    try:
        press_keys(hotkey)
        return jsonify({"status": "success", "message": f"Pressed hotkey: {hotkey}"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
