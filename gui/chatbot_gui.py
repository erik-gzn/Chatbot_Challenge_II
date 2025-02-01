
import customtkinter as ctk
import time
from tkinter import PhotoImage

# Funktion wird bei Drücken von "Senden" Button ausgeführt
def send_message():
    from chatbot_main import process_message
    # Stößt Verarbeitungsprozess in chatbot_main an
    process_message()


# Funktion gibt Text aus Eingabefeld zurück
def get_user_input():
    user_input = eingabefeld.get()
    return user_input

def schreibe_text(text, label):
    eingabefeld.delete(0, 'end')    # Reset des Eingabefeldes
    label.configure(text="")        # Reset des Textes
    for char in text:               # Funktion schreibt Buchstaben einzeln (ist schöner ;) ) 
        label.configure(text=label.cget("text") + char)
        label.update()
        time.sleep(0.03)  

# Hauptfenster (root) erstellen
fenster = ctk.CTk()
fenster.title("Bugchat GUI")
fenster.geometry("900x600")  # Vergrößertes Fenster
fenster.configure(bg_color="#2e3b4e")

# Theme auf dunkel setzen
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Layout - Zwei Spalten (direkt nebeneinander)
# Left Frame: Dunkelblau
frame_left = ctk.CTkFrame(fenster, width=400, height=600, corner_radius=0, fg_color="#2e3b4e")
frame_left.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")

# Right Frame: Helleres Blau für den Chat
frame_right = ctk.CTkFrame(fenster, width=500, height=600, corner_radius=0, fg_color="#3e4a61")
frame_right.grid(row=0, column=1, padx=0, pady=0, sticky="nsew")
frame_right.grid_rowconfigure(0, weight=1)  # Erste Zeile (Antwort-Label) soll sich dynamisch anpassen
frame_right.grid_rowconfigure(1, weight=0)  # Zweite Zeile (Eingabefeld) soll eine feste Höhe haben
frame_right.grid_rowconfigure(2, weight=0)  # Dritte Zeile (Senden-Button) soll auch eine feste Höhe haben

# Dynamische Konfigurierung: Beim vergrößern des Fensters vergrößern sich alle Bestandteile  mit
fenster.grid_rowconfigure(0, weight=1)
fenster.grid_columnconfigure(0, weight=1, uniform="equal")
fenster.grid_columnconfigure(1, weight=1, uniform="equal")

# Schriftzug "Bugchat"
chatbot_name_label = ctk.CTkLabel(frame_left, text="Bugchat", font=("Helvetica", 72, "bold"), fg_color="#2e3b4e", text_color="white")
chatbot_name_label.grid(row=0, column=0, padx=40, pady=40, sticky="w")

# Kleiner Kommentar unten
chatbot_explanation_label = ctk.CTkLabel(frame_left, text="Stichwörter: 'Notfall', 'Frage zu...' 'technisches Problem'", font=("Helvetica", 15, "bold"), fg_color="#2e3b4e", text_color="white")
chatbot_explanation_label.grid(row=2, column=0, padx=30, pady=40, sticky="w")

# Antwort des Chatbots
antwort_label = ctk.CTkLabel(frame_right, text="", font=("Helvetica", 24), fg_color="#3e4a61", text_color="white", anchor="w", justify="left", wraplength=400)
antwort_label.grid(row=0, column=0, padx=40, pady=40, sticky="w")

# Eingabefeld für den Nutzer (unten links) 
eingabefeld = ctk.CTkEntry(frame_right, font=("Helvetica", 24), fg_color="#4b5a6f", text_color="white", width=350, placeholder_text="Wie kann ich Ihnen helfen?") #Insert Color entfernt
eingabefeld.grid(row=1, column=0, padx=40, pady=10, sticky="ew")  # Verbreitert das Eingabefeld, sticky="ew" sorgt dafür, dass es sich horizontal ausdehnt "ew" --> east west Ausdehnung

# Senden-Button (unten rechts) 
senden_button = ctk.CTkButton(frame_right, text="Senden", font=("Helvetica", 24), fg_color="#4b5a6f", text_color="white", command=send_message)
senden_button.grid(row=2, column=0, padx=40, pady=10, sticky="w")  # Der Button bleibt rechts ausgerichtet

# Bild in der unteren linken Ecke des linken Frames (Bugchat-Seite)
bild = PhotoImage(file="BUGLAND_Logo.png")  
image_label = ctk.CTkLabel(frame_left, image=bild, text="")
image_label.grid(row=1, column=0, padx=40, pady=40, sticky="sw")

# Hauptloop starten
fenster.mainloop()
