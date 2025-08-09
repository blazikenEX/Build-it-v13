def chatbot_responses(user_input):
  user_input = user_input.lower()
  if "map" in user_input or "direction" in user_input:
    return "You can find useful directions about the Aalto campus from this map - usefulaaltomap.fi  . "
  elif "food" in user_input or "lunch" in user_input or "meal" in user_input:
    return "You can check this website for live menu for all the student restaurant at aalto - kanttiinit.fi   ."
  elif "marketplace" in user_input or "buy" in user_input:
    return "There is a second-hand buy and sell group for aalto students - t.me/aaltomarketplace"
  elif "joke" in user_input:
    return "Why couldn't the bicycle stand up by itself? Because it was two-tired!"
  else:
    return ("sorry don't know")

