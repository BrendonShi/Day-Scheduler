import os
from flask import Flask, render_template, request, jsonify
# import psycopg2
from psycopg2.extras import RealDictCursor
from get_db import get_db_connection, init_db


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_tasks', methods=['GET'])
def get_tasks():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    
    cur.execute('SELECT * FROM tasks')
    
    tasks = cur.fetchall()
    
    cur.close()
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
    cur = conn.cursor(cursor_factory=RealDictCursor)

    cur.execute('INSERT INTO tasks (name, start_time, end_time, color) VALUES (%s, %s, %s, %s) RETURNING id',
                   (data['name'], data['start'], data['end'], data['color']))
    
    new_id = cur.fetchone()['id']
    
    conn.commit()
    cur.close()
    conn.close()
    
    return jsonify({'id': new_id, 'status': 'success'})

@app.route('/delete_task', methods=['POST'])
def delete_task():
    data = request.json
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('DELETE FROM tasks WHERE id = %s', (data['id'],))
    
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({'status': 'deleted'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)