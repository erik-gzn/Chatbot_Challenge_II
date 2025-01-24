from data.chatbot_datasource import access_answer_for_node

def get_response(node_to_answer):
    
    return str(access_answer_for_node(node_to_answer))
    #return "So you have " + input_to_answer + "?"

get_response(1)