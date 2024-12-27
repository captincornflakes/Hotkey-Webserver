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
   git clone https://github.com/captincornflakes/hotkey-web-server.git
   cd hotkey-web-server
    ```


3. **Install Dependencies**:
   ```
   pip install flask pynput
    ```

4. **JSON**:
   ```
    [
        {
            "group": "Streaming / Recording",
            "buttons": [
                { "label": "Toggle Stream", "hotkey": "ctrl+w", "color": "success" },
                { "label": "Toggle Record", "hotkey": "ctrl+r", "color": "danger" }
            ]
        },
        {
            "group": "Scene",
            "buttons": [
                { "label": "Tiktok 1", "hotkey": "ctrl+1", "color": "info" },
                { "label": "Tiktok 2", "hotkey": "ctrl+2", "color": "info" }
            ]
        },
        {
            "group": "Refresh",
            "buttons": [
                { "label": "Scene 1", "hotkey": "ctrl+3", "color": "secondary" },
                { "label": "Scene 2", "hotkey": "ctrl+4", "color": "secondary" }
            ]
        }
    ]


    ```


4. **Run**:
   ```
   sudo python3 web_hotkey_server.py
    ```
---
##  Open a browser and navigate to the server:
   
http://127.0.0.1 Click on the buttons to simulate the configured keypresses.

Customize the button labels and hotkeys by modifying the button_config.json file and restarting the server.
---
##  Project Structure:
    hotkey_web_server/
    ├── button_groups/               # Directory containing button group configurations
    │   ├── default.json             # Example button group configuration
    │   └── another_config.json      # Another example configuration
    ├── static/                      # Directory for static files (CSS, JS, images)
    │   ├── css/
    │   │   └── styles.css           # CSS file for custom styling
    │   ├── js/
    │   │   └── script.js            # JavaScript file for client-side functionality
    ├── templates/                   # Directory for HTML templates
    │   └── index.html               # Main HTML template for the web interface
    ├── web_hotkey_server.py         # Main Python Flask server script
    └── requirements.txt             # Python dependencies

---
##  Dependencies:
Flask - Lightweight web framework for Python.

pynput - Library to control and monitor keyboard events.

Install dependencies with:

    pip install flask pynput

---
## Contributing:
   
Contributions are welcome! Feel free to submit a pull request or open an issue for any bugs or feature requests.
  
---
## License:

This project is licensed under the MIT License. See the LICENSE file for details.


