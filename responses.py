import random
responses = [
    "Hello! How can I help you?",
    "What's on your mind?",
    "I'm here to assist you. What do you need?",
    "How can I assist you?",
    "What can I help you with?",
]

def chatbot_responses(user_input):
  user_input = user_input.lower()

  if "movie" in user_input:
    return "I recommend checking out the IMDb website for movie recommendations. They have a wide variety of genres and ratings to choose from."
  elif "weather" in user_input:
    return "You can check the weather by using a weather website or app. Some popular ones include Weather.com and The Weather Channel app."
  elif "news" in user_input:
    return "There are many websites and apps that offer the latest news updates, such as CNN, Fox News, and NBC News."
  elif "joke" in user_input:
    return "Why couldn't the bicycle stand up by itself? Because it was two-tired!"
  else:
    return random.choice(responses)

