# from gui.chatbot_gui import send_message

# while True:
#     send_message() 


# chatbot_main.py

from gui.chatbot_gui import get_user_input, schreibe_text, antwort_label
from logic.chatbot_logic import ChatBot



chatbot = ChatBot()


def process_message():
            
    user_input = get_user_input()  
    if user_input:
        response = chatbot.get_response(user_input)  
        schreibe_text(response, antwort_label)  
