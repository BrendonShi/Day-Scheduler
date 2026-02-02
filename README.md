# To-Do List Website

![NVIDIA_Overlay_6eUH37isLV](https://github.com/user-attachments/assets/48626073-fa57-4e18-9a36-7239cd771ab4)

It is a simple, effective productivity tool built with Flask, HTML, CSS, and JavaScript, with Sqlite3 database. It allows you to schedule specific time blocks and plays a custom alarm sound at the start and end of every task.

All schedules are automatically saved to a sqlite3 database.

## Prerequisites
You need **Python** installed on your computer.

## Installation

1. **Clone or Download** this repository to your local machine.
   ```bash
   git clone "repository-link"
   ```
2. **Navigate to the project folder** in your terminal/command prompt:
   ```bash
   cd to-do-list-website
   ```

### (Windows)

***Python must be installed on the machine.***

Launch `setup.bat`, it will create python virtual environment, and install `flask`, `psycopg2-binary`, `python-dotenv` libraries.

### (MacOS)

***Python must be installed on the machine.***

You need to launch `setup.command`, but first, you must give it permission to run. Open your terminal, navigate to the folder, and type: chmod +x setup.command, then double click it. It will create python virtual environment, and install flask, psycopg2-binary, python-dotenv libraries.

---

## How to Run

1. **Activate Venv:**
   
   (Windows)
   ```bash
   ./venv/Scripts/activate
   ```

   (MacOS)
   ```bash
   source .venv/bin/activate
   ```

1.  **Start the Application:**
    Run the following command in your terminal:
    ```bash
    python app.py
    ```
2.  **Open in Browser:**
    Open your web browser and go to:
    `http://127.0.0.1:5000`

## Customization

### Changing the Alarm Sound
1.  Place your audio file (MP3 or WAV) inside the `static` folder.
2.  Rename the file to `alarm.mp3`.

### Resetting the Database
If you want to clear all tasks or if you encounter database errors after changing the code:
1.  Stop the server (Ctrl+C).
2.  Delete the `schedule.db` file in the project folder.
3.  Restart the server (`python app.py`). A new, empty database will be created.

## Project Structure

```text
to-do-list-website/
├── app.py
├── get_db.py
├── schedule.db
├── setup.bat
├── setup.command
├── requirements.txt
├── .env
├── static/
│   ├── style.css
│   ├── script.js
│   └── alarm.mp3
└── templates/
    └── index.html
