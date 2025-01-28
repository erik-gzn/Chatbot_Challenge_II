from data.chatbot_datasource import access_chatbots_answer
from data.chatbot_datasource import access_id_of_given_question
from language_processing.chatbot_nlp import answer_transformer


terminal_status = False
talk_status = 1
user_input = None

def get_response(given_answer):
    global talk_status
    if not given_answer:
        
        return access_chatbots_answer(talk_status)
        
    else:
        transformed_given_answer = answer_transformer(given_answer)
        next_ans_id = access_id_of_given_question(transformed_given_answer[0], talk_status)
        talk_status = access_chatbots_answer(next_ans_id)[0]
        return access_chatbots_answer(next_ans_id)
    
    
        

#get_response(0)