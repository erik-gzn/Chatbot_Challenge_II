import sqlite3
from rapidfuzz import process

def answer_transformer(answer_to_transform, talk_status):
    database_entries = load_database_entries("chatbot_data.db", "Answers")
    texts = [entry[2] for entry in database_entries if int(entry[1]) == talk_status] # wandelt Datenbankzeilen in Liste von Strings (answer_text) um
    best_match = process.extractOne(answer_to_transform, texts)
    print(best_match)
    return best_match



# Funktion von ChatGPT:

def load_database_entries(db_path, table_name):
    """
    Lädt Einträge aus einer SQL-Datenbank und gibt sie als Liste von Tuples zurück.

    Args:
        db_path (str): Pfad zur SQLite-Datenbank.
        table_name (str): Name der Tabelle in der Datenbank.

    Returns:
        list: Liste von Tuples im Format (parent_id, text, child_id).
    """
    # Verbindung zur Datenbank herstellen
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # SQL-Abfrage erstellen
    query = f"SELECT id, node_id, answer_text, next_node_id FROM {table_name}"

    # Abfrage ausführen
    cursor.execute(query)

    # Ergebnisse abrufen und in eine Liste von Tuples umwandeln
    results = cursor.fetchall()

    # Verbindung schließen
    conn.close()

    return results

