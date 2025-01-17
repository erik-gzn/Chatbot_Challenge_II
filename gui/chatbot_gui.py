import tkinter as tk
from logic.chatbot_logic import get_response

def send_message():
    user_input = str(entry.get())
    response = str(get_response(user_input))
    text_area.insert(tk.END, "You: " + user_input + "\n")
    text_area.insert(tk.END, "Bot: " + response + "\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chatbot")


text_area = tk.Text(root, height=50, width=100)
text_area.pack()

entry = tk.Entry(root, width=80)
entry.pack()

send_button = tk.Button(root, text="Senden", command=send_message)
send_button.place(x=0, y=800)

root.mainloop()