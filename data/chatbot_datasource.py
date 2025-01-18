# Setup the database for the chatbot service

import sqlite3

def setup_database():
    conn = sqlite3.connect('chatbot_service_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS chatbot_data (
            id INTEGER PRIMARY KEY,
            tag_one TEXT,
            tag_two TEXT,
            tag_three TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(tag_one, tag_two, tag_three, answer):
    conn = sqlite3.connect('chatbot_service_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO chatbot_data (tag_one, tag_two, tag_three, answer)
        VALUES (?, ?, ?, ?)
    ''', (tag_one, tag_two, tag_three, answer))
    conn.commit()
    conn.close()

def access_data(tag=None):
    conn = sqlite3.connect('chatbot_service_data.db')
    cursor = conn.cursor()
    if tag:
        cursor.execute('''
            SELECT answer FROM chatbot_data
            WHERE tag_one = ? OR tag_two = ? OR tag_three = ?
        ''', (tag, tag, tag))
    else:
        cursor.execute('SELECT answer FROM chatbot_data')
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]

def delete_data(id):
    conn = sqlite3.connect('chatbot_service_data.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM chatbot_data WHERE id = ?', (id,))
    conn.commit()
    conn.close()


#setup_database()

# Daten in die Datenbank einfügen 
#insert_data('support', 'broken', '', 'We are sorry to hear that your device is broken and concerned to help you! Would you like us to book support or order parts for you?.')