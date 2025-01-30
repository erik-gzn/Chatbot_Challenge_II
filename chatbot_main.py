from gui.chatbot_gui import get_user_input, schreibe_text, antwort_label
from logic.chatbot_logic import ChatBot
import time


chatbot = ChatBot()


def process_message():
            
    user_input = get_user_input()  
    if user_input:
        response = chatbot.get_response(user_input)
        
        if response[4]:
            schreibe_text(response[1], antwort_label)
            time.sleep(0.5)
            schreibe_text(response[4], antwort_label)
        else:
            schreibe_text(response[1], antwort_label)
        