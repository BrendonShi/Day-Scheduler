# Day Timer

![msedge_88uUC2o0bI](https://github.com/user-attachments/assets/fa9f9eea-97b3-4eab-b733-a0a0cbf330b9)

It is a simple, effective productivity tool built with Flask, HTML, CSS, and JavaScript. It allows you to schedule specific time blocks and plays a custom alarm sound at the start and end of every task.

All schedules are automatically saved to a local SQLite database, so your plan persists even after you close the browser.

## Prerequisites
You need **Python**, **Flask** installed on your computer.

## Installation (Windows)

1. **Clone or Download** this repository to your local machine.
   ```bash
   git clone "repository-link"
   ```
3. **Navigate to the project folder** in your terminal/command prompt:
   ```bash
   cd day-scheduler
   ```
4. **Create virtual environment**
   ```bash
   python -m venv .venv
   ```
5. **Activate virtual environment**
   ```bash
   .venv/Scripts/activate
   ```
3. **Install Flask** (the web framework):
   ```bash
   pip install flask
   ```

## How to Run

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
daily_timer/
├── app.py
├── schedule.db   # will generate automatically
├── static/
│   ├── style.css
│   ├── script.js
│   └── alarm.mp3
└── templates/
    └── index.html
