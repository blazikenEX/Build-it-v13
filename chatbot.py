import webbrowser
from tkinter import Tk, Text, Entry, Button, END, Label
from responses import chatbot_responses  # or wherever your function is
from urls import URLS  # Import your URL dictionary

def open_link(label):
    webbrowser.open_new(label)

def send_message():
    # Get the user's input
    user_input = input_field.get()

    # Generate a response from the chatbot
    response = chatbot_responses(user_input)

    # Display the conversation in the text area
    text_area.insert(END, f"User: {user_input}\n")
    text_area.insert(END, f"Chatbot: ")

    # Loop through all URLs in urls.py
    for key, site in URLS.items():
        if site in response:  # if the URL text is in the response
            before, link, after = response.partition(site)

            # insert the beginning  of the sentence
            text_area.insert(END, before)

            # 2) link label (blue + underlined + clickable)
            link_clean = link.strip(" \n\t.,;:!?")
            url = link_clean if link_clean.startswith(("http://", "https://")) else "https://" + link_clean
            link_lbl = Label(
                root,
                text=link_clean,
                fg="blue",
                cursor="hand2",
                font=("Arial", 10, "underline"),
            )

            link_lbl.bind("<Button-1>", lambda e, u=url: webbrowser.open_new(u))

            # embed label inside Text widget here:
            text_area.window_create(END, window=link_lbl)
            # insert the rest of the sentence
            text_area.insert(END, after)
            break
    else:
        # No link found, just insert the response normally
        text_area.insert(END, response)

    text_area.insert(END, "\n\n")

# Create main window
root = Tk()
root.title("Chatbot")

# Create the chatbot's text area
text_area = Text(root, bg="white", width=50, height=20)
text_area.pack()

# Insert a greeting before user types anything
greeting = "Hello! How can I help you?\n\n"
text_area.insert(END, f"Chatbot: {greeting}")

# Create the user's input field
input_field = Entry(root, width=50)
input_field.pack()

# Create the send button
send_button = Button(root, text="Send", command=send_message)
send_button.pack()

# Gives you the possibility to send messages by clicking enter on your keyboard
input_field.bind("<Return>", lambda e: send_message())

root.mainloop()

