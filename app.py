import os
from flask import Flask, render_template, request, jsonify
from get_db import get_db_connection, init_db


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    tasks = conn.execute('SELECT * FROM tasks').fetchall()
    conn.close()

    tasks_list = [{
        'id': row['id'], 
        'name': row['name'], 
        'start': row['start_time'], 
        'end': row['end_time'], 
        'color': row['color']
    } for row in tasks]
    return jsonify(tasks_list)

@app.route('/add_task', methods=['POST'])
def add_task():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name, start_time, end_time, color) VALUES (?, ?, ?, ?)',
                   (data['name'], data['start'], data['end'], data['color']))
    conn.commit()
    new_id = cursor.lastrowid
    conn.close()
    return jsonify({'id': new_id, 'status': 'success'})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.json
    conn = get_db_connection()
    conn.execute('DELETE FROM tasks WHERE id = ?', (data['id'],))
    conn.commit()
    conn.close()
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)