from tkinter import Tk, Text, Entry, Button, END
from responses import chatbot_responses  # or wherever your function is

def send_message():
    # Get the user's input
    user_input = input_field.get()

    # Clear the input field
    input_field.delete(0, END)

    # Generate a response from the chatbot
    response = chatbot_responses(user_input)

    # Display the conversation in the text area
    text_area.insert(END, f"User: {user_input}\n")
    text_area.insert(END, f"Chatbot: {response}\n\n")

# Create main window
root = Tk()
root.title("Chatbot")

# Create the chatbot's text area
text_area = Text(root, bg="white", width=50, height=20)
text_area.pack()

# Insert a greeting before user types anything
greeting = "Hello! I'm your chatbot. How can I help you today?\n\n"
text_area.insert(END, f"Chatbot: {greeting}")

# Create the user's input field
input_field = Entry(root, width=50)
input_field.pack()

# Create the send button
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()

