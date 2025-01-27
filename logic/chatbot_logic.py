from data.chatbot_datasource import access_chatbots_answer
from data.chatbot_datasource import access_id_of_given_question



def get_response(given_answer, given_talk_status):
    
    if not given_answer:
        
        return access_chatbots_answer(given_talk_status)
        
    else:
        next_ans_id = access_id_of_given_question(given_answer, given_talk_status)
        return access_chatbots_answer(next_ans_id)
    
    
        

#get_response(0)