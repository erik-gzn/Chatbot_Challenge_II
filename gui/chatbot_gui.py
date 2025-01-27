import tkinter as tk
from logic.chatbot_logic import get_response



# def send_message():
    
#     user_input = str(entry.get())
    
#     response = str(get_response(user_input))
    
#     text_area.insert(tk.END, "You: " + user_input + "\n")
#     text_area.insert(tk.END, "Bot: " + response + "\n")
#     entry.delete(0, tk.END)

# root = tk.Tk()
# root.title("Chatbot")


# text_area = tk.Text(root, height=20, width=50)
# text_area.pack()

# entry = tk.Entry(root, width=80)
# entry.pack()

# send_button = tk.Button(root, text="Senden", command=send_message)
# send_button.place(x=0, y=300)

#root.mainloop()
def send_message():
    
    terminal_status = False
    talk_status = 1
    user_input = None
    
    while terminal_status == False:
             
        
        chatbots_answer = get_response(user_input, talk_status)
        
        
        print(len(chatbots_answer))
        if chatbots_answer[2] == 1:
            print(chatbots_answer[1])
            print(chatbots_answer[4])
            terminal_status = True
            break
        else:
            print(chatbots_answer[1])
            talk_status = chatbots_answer[0]

        user_input = input("Antwort: ")