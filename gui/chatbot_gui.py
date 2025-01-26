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
    print("Hallo hier ist Ihr Chatbot!")

    terminal_status = False

    while terminal_status == False:
        user_input = input("Antwort: ")
        chatbots_answer = get_response(user_input)
        print(len(chatbots_answer))
        if chatbots_answer[1] == 1:
            print(chatbots_answer[0])
            print("Service Info: " + chatbots_answer[2])
            terminal_status = True
            break
        else:
            print(chatbots_answer[0])
