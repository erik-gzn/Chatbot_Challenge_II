from data.chatbot_datasource import access_chatbots_answer, access_id_of_given_question
from language_processing.chatbot_nlp import answer_transformer

    
class ChatBot: 
    def __init__(self):
        self.talk_status = 1
        self.terminal_status = False
        self.misunderstandings = 0

  
    def get_response(self, user_input):
        # Verarbeite die Antwort des Nutzers
        transformed_input = self._transform_input(user_input)
        if float(transformed_input[1]) > 60.0:
            next_answer_id = self._get_next_answer_id(transformed_input)
            response = self._fetch_answer(next_answer_id)
            return response
        else:
            
            self.misunderstandings += 1
            if self.misunderstandings <= 3:
                response = (self.talk_status, "Das habe ich leider nicht verstanden, bitte wiederholen Sie Ihre Antwort", 0, self.talk_status, None)
                return response
            else: 
                response = (self.talk_status, "Wir möchten nicht, dass Sie hier gefangen bleiben. Daher bitten wir Sie, Kontakt mit unserem Service aufzunehmen.", 1, self.talk_status, "Tel.: 0800 459 8732, E-Mail: contact.support@bugland.de, Mo-Fr von 8:00 - 16:00 Uhr")
                return response

    def _transform_input(self, user_input):
        # Hier transformierst du die Eingabe des Nutzers
        return answer_transformer(user_input, self.talk_status)

    def _get_next_answer_id(self, transformed_input):
        # Hole die ID der nächsten Antwort basierend auf der transformierten Eingabe
        return access_id_of_given_question(transformed_input[0], self.talk_status)

    def _fetch_answer(self, answer_id):
        # Hole die Antwort anhand der ID
        response = access_chatbots_answer(answer_id)
        self.talk_status = response[0]  # Aktualisiere den Gesprächszustand
        return response