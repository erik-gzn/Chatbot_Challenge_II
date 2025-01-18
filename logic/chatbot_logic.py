from data.chatbot_datasource import access_data

def get_response(input_to_answer):
    
    return str(access_data(input_to_answer))
    #return "So you have " + input_to_answer + "?"