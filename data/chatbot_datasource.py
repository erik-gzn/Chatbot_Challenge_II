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


# Eigene Einträge nach Prozesschart :
# insert_node('Wie kann ich Ihnen helfen?', 0, 0, None) # Startknoten
# insert_node('Handelt es sich bei Ihrem Problem um einen Notfall?', 0, 1, None) 
# insert_node('Bitte eröffnen Sie ein Ticket im unten dargestellten Link. Gibt es ein weiteres Problem?', 0, 2, 'Ticketservice: www.bugland.de/ticketservice')
# insert_node('Vielen Dank für die Nutzung unseres Ticketservices! Wir werden uns umgehend um Ihre Problem kümmern und uns wieder bei Ihnen melden!', 1, 3,)
# insert_node('Wie können wir Ihnen sonst behilflich sein? Haben Sie ein technisches Problem, Fragen zur Abrechnung oder allgemeine Fragen?', 0, 4, None)
# insert_node('Um welches Produkt handelt es sich?', 0, 5, None) 


# Windowfly: 
# insert_node('In den Serviceinformationen finden Sie typische Problemstellungen sowie das Manual zur Windowfly. Sind diese Informationen zunächst ausreichend?', 0, 6, 'Serviceinformation zur Windowfly: www.bugland.de/guides/windowfly')
# insert_node('Es tut uns leid, dass unsere Infotheke Ihnen nicht geholfen. Im nächsten Schritt können Sie unter der Serviceinformation ein Ticket erstellen. Ein Mitarbeiter oder eine Mitarbeiterin wird sich schnellstmöglich um Ihr Problem kümmern!', 1, 7, 'Ticketservice: www.bugland.de/ticketservice')
# insert_node('Es freut uns, dass wir Ihnen bei Ihrem Problem behilflich sein konnten. Wir würden uns über ein Feedback freuen, um unseren Service entsprechend beizubehalten oder zu verbessern!', 1, 8, 'Feedback: www.bugland.de/feedback')

# Cleanbug: 
# insert_node('In den Serviceinformationen finden Sie typische Problemstellungen sowie das Manual zum Cleanbug. Sind diese Informationen zunächst ausreichend?', 0, 10, 'Serviceinformation zur Windowfly: www.bugland.de/guides/cleanbug')

# Gardenbeetle: 
# insert_node('In den Serviceinformationen finden Sie typische Problemstellungen sowie das Manual zum Gardenbeetle. Sind diese Informationen zunächst ausreichend?', 0, 11, 'Serviceinformation zur Windowfly: www.bugland.de/guides/gardenbeetle')




# insert_answer(1, 'ja', 2)
# insert_answer(1, 'nein', 4)
# insert_answer(2, 'ja', 1)
# insert_answer(2, 'nein', 3)
# insert_answer(4, 'technisch', 5)


# insert_answer(5, 'windowfly', 6)
# insert_answer(6, 'nein', 7)
# insert_answer(6, 'ja', 8)

# insert_answer(5, 'cleanbug', 10)
# insert_answer(10, 'nein', 7)
# insert_answer(10, 'ja', 8)

# insert_answer(5, 'gardenbeetle', 11)
# insert_answer(11, 'nein', 7)
# insert_answer(11, 'ja', 8)

