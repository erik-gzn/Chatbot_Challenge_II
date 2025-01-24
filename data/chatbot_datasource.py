# Setup the database for the chatbot service

import sqlite3

def setup_database():
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Nodes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            is_terminal INTEGER NOT NULL,
            parent_id INTEGER,
            service_info TEXT,
            FOREIGN KEY (parent_id) REFERENCES Nodes (id)
                       
        );
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            node_id INTEGER NOT NULL,
            answer_text TEXT NOT NULL,
            next_node_id INTEGER,
            FOREIGN KEY (node_id) REFERENCES Nodes (id),
            FOREIGN KEY (next_node_id) REFERENCES Nodes (id)
                       
        );            
    ''')
    conn.commit()
    conn.close()


setup_database()




# INSERT-Funktion: 


def insert_node(question, is_terminal, parent_id=None, service_info=None):
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Nodes (question, is_terminal, parent_id, service_info)
        VALUES (?, ?, ?, ?);
    ''', (question, is_terminal, parent_id, service_info))
    conn.commit()
    conn.close()

def insert_answer(node_id, answer_text, next_node_id=None):
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Answers (node_id, answer_text, next_node_id)
        VALUES (?, ?, ?);
    ''', (node_id, answer_text, next_node_id))
    conn.commit()
    conn.close()

def access_answer_for_node(given_parent_id):
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT question, is_terminal, service_info FROM Nodes WHERE parent_id = ?", (given_parent_id,))
    node = cursor.fetchone()
    if not node:
        
        return "Kein passender Eintrag!"
    else:
        return node[0]
    

#Ersteinrichtung Datenbank:

#setup_database()

# Ersten zwei Einträge:
#insert_node('Wie kann ich Ihnen helfen?', 0, 0, None)
#insert_answer(1,"technisch", 2)


#print(access_answer_for_node(0))