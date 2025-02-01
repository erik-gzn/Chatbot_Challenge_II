import sqlite3
from rapidfuzz import process           # Bibliothek für Stringmatching 

def answer_transformer(answer_to_transform, talk_status):
    database_entries = load_database_entries("chatbot_data.db", "Answers")           # Funktion lädt alle Datenbankeinträge
    texts = [entry[2] for entry in database_entries if int(entry[1]) == talk_status] # wandelt Datenbankzeilen in Liste von Strings (answer_text) um; filtern, welche nach jetzigem Gesprächsstatus überhaupt in Frage kommen
    best_match = process.extractOne(answer_to_transform, texts)                      # bestes Match wird zurückgegeben; Typ der Rückgabe ist ein Tuple z.B.: ('windowfly', 90.0, 0) --> ("Antwortsatz" [String], Match in % [Float], Position in der durchsuchten Liste [Int])
    #print(best_match)                                                               
    return best_match



def load_database_entries(db_path, table_name):
    # Verbindung zur Datenbank 
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL-Abfrage 
    query = f"SELECT id, node_id, answer_text, next_node_id FROM {table_name}"

    # Abfrage ausführen
    cursor.execute(query)

    # Speicherung der Ergebnisse in Liste
    results = cursor.fetchall()

    # Verbindung beenden
    conn.close()

    return results

