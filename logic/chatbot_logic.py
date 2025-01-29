from data.chatbot_datasource import access_chatbots_answer, access_id_of_given_question
from language_processing.chatbot_nlp import answer_transformer


# terminal_status = False
# talk_status = 1
# user_input = None

# def get_response(given_answer):
#     global talk_status
    
#     if not given_answer:
        
#         return access_chatbots_answer(talk_status)
        
#     else:
#         transformed_given_answer = answer_transformer(given_answer)
#         next_ans_id = access_id_of_given_question(transformed_given_answer[0], talk_status)
#         talk_status = access_chatbots_answer(next_ans_id)[0]
#         return access_chatbots_answer(next_ans_id)
    
class ChatBot: 
    def __init__(self):
        self.talk_status = 1
        self.terminal_status = False

  
    def get_response(self, user_input):
        # Verarbeite die Antwort des Nutzers
        transformed_input = self._transform_input(user_input)
        next_answer_id = self._get_next_answer_id(transformed_input)
        response = self._fetch_answer(next_answer_id)
        return response

    def _transform_input(self, user_input):
        # Hier transformierst du die Eingabe des Nutzers
        return answer_transformer(user_input)

    def _get_next_answer_id(self, transformed_input):
        # Hole die ID der nächsten Antwort basierend auf der transformierten Eingabe
        return access_id_of_given_question(transformed_input[0], self.talk_status)

    def _fetch_answer(self, answer_id):
        # Hole die Antwort anhand der ID
        response = access_chatbots_answer(answer_id)
        self.talk_status = response[0]  # Aktualisiere den Gesprächszustand
        return response[1]