# from rapidfuzz import process, fuzz
# from sentence_transformers import SentenceTransformer, util
# import sqlite3


# def load_database_entries(db_path, table_name):
#     """
#     Lädt Einträge aus einer SQL-Datenbank und gibt sie als Liste von Tuples zurück.

#     Args:
#         db_path (str): Pfad zur SQLite-Datenbank.
#         table_name (str): Name der Tabelle in der Datenbank.

#     Returns:
#         list: Liste von Tuples im Format (parent_id, text, child_id).
#     """
#     # Verbindung zur Datenbank herstellen
#     conn = sqlite3.connect(db_path)
#     cursor = conn.cursor()

#     # SQL-Abfrage erstellen
#     query = f"SELECT parent_id, text, child_id FROM {table_name}"

#     # Abfrage ausführen
#     cursor.execute(query)

#     # Ergebnisse abrufen und in eine Liste von Tuples umwandeln
#     results = cursor.fetchall()

#     # Verbindung schließen
#     conn.close()

#     return results








# # Initialisiere das semantische Modell
# model = SentenceTransformer('all-MiniLM-L6-v2')

# # Datenbankeinträge (aus SQL geladen)
# database_entries = load_database_entries("chatbot_data.db", "Answers")

# # Benutzeranfrage
# user_input = "Ich brauche Hilfe mit meinem Internet"


# # Fuzzy Matching
# def find_best_match_fuzzy(user_input, database_entries):
#     texts = [entry[1] for entry in database_entries]
#     best_match = process.extractOne(user_input, texts, scorer=fuzz.partial_ratio)
#     best_entry = database_entries[texts.index(best_match[0])]
#     return best_entry, best_match[1] / 100  # Score als Wert zwischen 0 und 1 zurückgeben


# # Semantische Suche
# def find_best_match_semantic(user_input, database_entries):
#     texts = [entry[1] for entry in database_entries]
#     entry_embeddings = model.encode(texts, convert_to_tensor=True)
#     user_embedding = model.encode(user_input, convert_to_tensor=True)

#     cosine_scores = util.pytorch_cos_sim(user_embedding, entry_embeddings)
#     best_match_idx = cosine_scores.argmax().item()
#     best_entry = database_entries[best_match_idx]
#     best_score = cosine_scores[0][best_match_idx].item()
#     return best_entry, best_score


# # Kombinierte Suche
# def combined_search(user_input, database_entries, weight_fuzzy=0.3, weight_semantic=0.7):
#     # Kombinierte Scores berechnen
#     combined_scores = []
#     for entry in database_entries:
#         fuzzy_score = fuzz.partial_ratio(user_input, entry[1]) / 100
#         semantic_score = util.pytorch_cos_sim(
#             model.encode(user_input, convert_to_tensor=True),
#             model.encode(entry[1], convert_to_tensor=True)
#         )[0].item()
#         combined_score = weight_fuzzy * fuzzy_score + weight_semantic * semantic_score
#         combined_scores.append((entry, combined_score))

#     # Besten Treffer finden
#     best_entry, best_score = max(combined_scores, key=lambda x: x[1])
#     return best_entry, best_score


# # Ergebnisse abrufen
# fuzzy_result = find_best_match_fuzzy(user_input, database_entries)
# semantic_result = find_best_match_semantic(user_input, database_entries)
# combined_result = combined_search(user_input, database_entries)

# # Ergebnisse ausgeben
# print("Fuzzy Match:")
# print(f"Eintrag: {fuzzy_result[0]}, Score: {fuzzy_result[1]:.2f}")

# print("\nSemantisches Match:")
# print(f"Eintrag: {semantic_result[0]}, Score: {semantic_result[1]:.2f}")

# print("\nKombiniertes Match:")
# print(f"Eintrag: {combined_result[0]}, Score: {combined_result[1]:.2f}")


