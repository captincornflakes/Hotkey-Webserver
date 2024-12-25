# Hotkey-Webserver
 
# Hotkey Web Server

A Python-based web server that provides a web interface for simulating keypresses based on configurable buttons. This project is perfect for controlling applications or workflows with hotkeys through a browser interface.

---

## Features
- Web interface with buttons generated dynamically from a JSON configuration file.
- Simulates keypresses using the [pynput](https://pypi.org/project/pynput/) library.
- Configurable hotkeys and button labels for easy customization.
- Lightweight and easy to set up.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/hotkey-web-server.git
   cd hotkey-web-server
    ```


3. **Install Dependencies**:
   ```
   pip install flask pynput
    ```

4. **JSON**:
   ```
   [
    { "label": "Start Stream", "hotkey": "shift+w" },
    { "label": "Stop Stream", "hotkey": "ctrl+w" },
    { "label": "Start Record", "hotkey": "shift+r" },
    { "label": "Stop Record", "hotkey": "ctrl+r" },
    { "label": "Tiktok Scene 1", "hotkey": "shift+1" },
    { "label": "Tiktok Scene 2", "hotkey": "shift+2" },
    { "label": "Refresh Scene 1", "hotkey": "ctrl+1" },
    { "label": "Refresh Scene 2", "hotkey": "ctrl+2" }
    ]

    ```


4. **Run**:
   ```
   sudo python3 web_hotkey_server.py
    ```
 **Open a browser and navigate to the server**:
   ```
    http://127.0.0.1
    Click on the buttons to simulate the configured keypresses.

    Customize the button labels and hotkeys by modifying the button_config.json file and restarting the server.
   ```


**Project Structure**:
    ```php
    hotkey-web-server/
    ├── web_hotkey_server.py   # Main Python script
    ├── button_config.json     # Configuration file for buttons and hotkeys
    ├── templates/
    │   └── index.html         # HTML template for the web interface
    ├── static/           
    ```

**Dependencies**:
   ```
    Flask - Lightweight web framework for Python.
    pynput - Library to control and monitor keyboard events.
    Install dependencies with:
    ```

    ```
    pip install flask pynput
    ```

    **Contributing**:
    Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.

    **License**:
    This project is licensed under the MIT License. See the LICENSE file for details.

