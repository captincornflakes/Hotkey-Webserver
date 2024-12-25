import os
import json
import psutil
from flask import Flask, render_template, request, jsonify
from pynput.keyboard import Controller, Key

# Flask app setup
app = Flask(__name__)
keyboard = Controller()

# Directory for button group files
BUTTON_GROUPS_DIR = "button_groups"

# Load all available button group files
def get_button_groups():
    files = [f for f in os.listdir(BUTTON_GROUPS_DIR) if f.endswith(".json")]
    return files

# Load a specific button group configuration
def load_config(filename):
    filepath = os.path.join(BUTTON_GROUPS_DIR, filename)
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"{filepath} does not exist.")
    with open(filepath, "r") as f:
        return json.load(f)


# Simulate a key press
def press_keys(hotkey):
    keys = hotkey.split("+")
    key_objects = []
    for key in keys:
        if hasattr(Key, key):  # Check for special keys (e.g., shift, ctrl)
            key_objects.append(getattr(Key, key))
        else:
            key_objects.append(key)  # Regular keys
    for key in key_objects[:-1]:
        keyboard.press(key)
    keyboard.press(key_objects[-1])
    keyboard.release(key_objects[-1])
    for key in reversed(key_objects[:-1]):
        keyboard.release(key)

# Routes
@app.route("/")
def index():
    groups = os.listdir(BUTTON_GROUPS_DIR)
    selected_group = groups[0] if groups else None
    return render_template("index.html", groups=groups, selected_group=selected_group)

@app.route("/load_group", methods=["POST"])
def load_group():
    data = request.get_json()
    filename = data.get("filename")
    if filename == "System Stats":
        return jsonify({
            "status": "success",
            "stats": get_system_stats()
        })
    
    filepath = os.path.join(BUTTON_GROUPS_DIR, filename)
    if not os.path.isfile(filepath):
        return jsonify({"status": "error", "message": f"Group {filename} not found."})
    
    with open(filepath, "r") as f:
        config = json.load(f)
    return jsonify({"status": "success", "config": config})

def get_system_stats():
    # CPU, RAM, and Temperature Stats
    stats = {
        "CPU Usage": f"{psutil.cpu_percent()}%",
        "RAM Usage": f"{psutil.virtual_memory().used / (1024 ** 3):.2f} GB / {psutil.virtual_memory().total / (1024 ** 3):.2f} GB",
    }

    # Add temperature sensor details (if supported)
    try:
        temps = psutil.sensors_temperatures()
        if temps:
            for name, entries in temps.items():
                for entry in entries:
                    stats[f"{name} ({entry.label or 'Core'})"] = f"{entry.current}°C"
    except AttributeError:
        stats["Temperature Sensors"] = "Not Supported"

    return stats

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
