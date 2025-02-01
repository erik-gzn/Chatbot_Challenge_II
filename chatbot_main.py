from gui.chatbot_gui import get_user_input, schreibe_text, antwort_label
from logic.chatbot_logic import ChatBot
import time

# Instanz chatbot von Klasse ChatBot (befindet sich in /logic/chatbot_logic) erstellen --> Klasse, die alle verarbeitenden Funktionen enthält)
chatbot = ChatBot()


# process_message ist das "Herzstück" --> holt sich eingabe aus GUI, übergibt sie an verarbeitende Funktion (chatbot.get_response) und schreibt das Ergebnis in die GUI
def process_message():
            
    user_input = get_user_input()  
    if user_input:
        response = chatbot.get_response(user_input.lower()) # .lower für größere Präzision in DB
        
        if response[4]:                                     # Wenn es an Index 4 Eintrag (Serviceinformation) gibt, soll auch der geprinted werden
            schreibe_text(response[1], antwort_label)
            time.sleep(0.5)
            schreibe_text(response[4], antwort_label)
        else:
            schreibe_text(response[1], antwort_label)       # Andernfalls wird nur der hauptsächliche Text geprinted

""" ---------------------------------------------------------------------------
Pseudocode für diese Funktion:


from gui/chatbot_gui import "get_user_input", "schreibe_text", "antwort_label" 


chatbot = new ChatBot()

function process_message:
	
	user_input = get_user_intput()

	if user_input != None:
	
		response = chatbot.get_response(lowercase(user_input))
	
		if response[4] != None:
		
			schreibe_text(response[1], antwort_label)
	
			pause(0.5s)
		
			schreibe_text(response[4], antwort_label)

		else:
			
			schreibe_text(response[1], antwort_label)

-------------------------------------------------------------------------"""
