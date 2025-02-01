from data.chatbot_datasource import access_chatbots_answer, access_id_of_given_question
from language_processing.chatbot_nlp import answer_transformer

# Diese Klasse ist der eigentliche chatbot, verarbeitet Eingabe und gibt Antwort zurück
class ChatBot: 
    def __init__(self): # Startwerte werden bei Initialisierung einer Instanz festgelegt
        self.talk_status = 1            # Startknoten der Unterhaltung
        self.terminal_status = False    # Wenn True, dann ist ein Gesprächszweig beendet
        self.misunderstandings = 0      # Anzahl an Antworten, die der Chatbot nicht verstanden hat

  
    def get_response(self, user_input):
        # Verarbeite die Antwort des Nutzers
        transformed_input = self._transform_input(user_input)               # Ruft aus /language_processing/chatbot_nlp die Funktion zur Sprachverarbeitung auf
        if float(transformed_input[1]) > 59.0:                              # 59% Match mit Datenbankeintrag gilt als Treffer
            next_answer_id = self._get_next_answer_id(transformed_input)    # ID der nächsten Chatbotantwort wird rausgesucht
            response = self._fetch_answer(next_answer_id)                   # Antwort = Datenbankeintrag der obigen ID
            return response
        else:                                                               # Im Else Statement werden Missverständnisse verarbeitet 
            self.misunderstandings += 1                                     
            if self.misunderstandings <= 3:                                 # bei misunderstandings > 3 löst Weiterleitung an Support aus
                response = (self.talk_status, "Das habe ich leider nicht verstanden, bitte wiederholen Sie Ihre Antwort", 0, self.talk_status, None)
                return response
            else: 
                response = (self.talk_status, "Wir möchten nicht, dass Sie hier gefangen bleiben. Daher bitten wir Sie, Kontakt mit unserem Service aufzunehmen.", 1, self.talk_status, "Tel.: 0800 459 8732, E-Mail: contact.support@bugland.de, Mo-Fr von 8:00 - 16:00 Uhr")
                return response

    def _transform_input(self, user_input):                                 # Funktion, zur Sprachverarbeitung | eigentliche Funktion ist hier answer_transformer --> /language_processing/chatbot_nlp
        return answer_transformer(user_input, self.talk_status)

    def _get_next_answer_id(self, transformed_input):                       # Sucht die ID der nächsten Antwort raus
        return access_id_of_given_question(transformed_input[0], self.talk_status)

    def _fetch_answer(self, answer_id):                                     # sucht die Antwort zur rausgesuchten ID in der anderen Tabelle
       
        response = access_chatbots_answer(answer_id)
        self.talk_status = response[0]  # Aktualisiere den Gesprächszustand
        return response