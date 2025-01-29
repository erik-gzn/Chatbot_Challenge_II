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


#setup_database()




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

def access_chatbots_answer(given_id):
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    #cursor.execute("SELECT question, is_terminal, service_info FROM Nodes WHERE id = ?", (given_id,))
    # ganze Zeile:
    cursor.execute("SELECT * FROM Nodes WHERE id = ?", (given_id,))

    node = cursor.fetchone()
    
    if not node:
        
        return "Kein passender Eintrag!"
    else:
        return node

# def access_id_of_given_question(given_user_input):
#     conn = sqlite3
#     conn = sqlite3.connect('chatbot_data.db')
#     cursor = conn.cursor()
#     cursor.execute("SELECT next_node_id FROM Answers WHERE answer_text = ?", (given_user_input,))
#     gotten_next_node_id = cursor.fetchone()
#     print(type(gotten_next_node_id))
#     return gotten_next_node_id[0]

# Bugfix Versuch, mit current_id:

def access_id_of_given_question(given_user_input, current_id):
    conn = sqlite3.connect('chatbot_data.db')
    cursor = conn.cursor()
    
    # SQL-Abfrage anpassen, um sowohl answer_text als auch current_id zu überprüfen
    cursor.execute("SELECT next_node_id FROM Answers WHERE answer_text = ? AND node_id = ?", (given_user_input, current_id))
    
    gotten_next_node_id = cursor.fetchone()

    if gotten_next_node_id:
        return gotten_next_node_id[0]
    else:
        # print("Kein Eintrag gefunden, der zu den gegebenen Parametern passt. Bitte probieren Sie Ihre Eingabe erneut: ")
        return current_id




#Ersteinrichtung Datenbank:
"""
setup_database()

# GPT Einträge zum Funktionstest:
insert_node('Wie kann ich Ihnen helfen?', 0, 0, None)
insert_node('Benötigen Sie technische Hilfe?', 0, 1, None)
insert_node('Was genau funktioniert nicht?', 0, 2, None)
insert_node('Kontaktieren Sie Support A', 1, 3, 'Support A: 12345')
insert_node('Kontaktieren Sie Support B', 1, 3, 'Support B: 67890')
insert_node('Möchten Sie Informationen zur Abrechnung?', 0, 1, None)
insert_node('Kontaktieren Sie das Abrechnungsteam', 1, 6, 'Abrechnungsteam: 54321')

insert_answer(1,'technische Hilfe', 2)
insert_answer(1,'Abrechnung', 6)
insert_answer(2,'Ja', 3)
insert_answer(2,'Nein', 1)
insert_answer(3,'Mein Internet funktioniert nicht.', 4)
insert_answer(3,'Mein Gerät funktioniert nicht', 5)
insert_answer(6,'Ja', 7)
insert_answer(6,'Nein', 1)
"""


# Produktionsdaten:

# setup_database()

# insert_node( "Willkommen bei Bugchat! Wie kann ich Ihnen helfen?", 0, 0, "Wenn es sich bei Ihrem Problem um einen Notfall handelt, schreiben Sie bitte: Notfall")
# insert_node( "Bleiben Sie ruhig, unter folgender Telefonnummer erreichen Sie unseren technischen Support...", 0, 1, "Technischer Support: 0800 459 8731 110 - Möchten Sie uns trotz Ihres Notfalls ein Feedback geben?")
# insert_node( "Vielen Dank, dass Sie sich die Zeit nehmen, uns ein Feedback zu geben. Wir sind stets bemüht, unseren Service für Sie zu verbesern!", 1, 2, "Link zum Feedback: www.bugland.de/feedback")
# insert_node( "Wir danken Ihnen ganz herzlich für die vertrauensvolle Nutzung unserer Services. Kontaktieren Sie uns, falls Sie weitere Hilfe benötigen!", 1, 2, "Bis zum nächsten mal...")


# insert_answer( 1, "Notfall", 2)
# insert_answer( 2, "Ja", 3)
# insert_answer( 2, "Nein", 4)
