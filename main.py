import random
  
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards) == 11 and len(cards) == 2:
      return 0
    if 11 in cards and sum(cards) > 21:
      cards.remove(11)
      cards.append(1)
  
    return sum(cards)
def compare(user_score, computer_score):
    if user_score == computer_score:
      return "Draw"
    elif computer_score == 0:
      return "You lose, opponent has BlackJack."
    elif user_score == 0:
      return "You lose, opponent has BlackJack."
    elif user_score > 21:
      return "You went over. You lose."
    elif computer_score > 21:
      return "Opponent went over. You Win."
    else:
      wi = max(user_score, computer_score)
      if wi == user_score:
        return "You Win."
      else:
        return "You lose."

def play_game():
  logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
  print(logo)
  user_cards = []
  computer_cards = []
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  ret = False
  while not ret:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
  
    print(f"Your cards: {user_cards}, current score: {user_score}.")
    print(f"Your opponent's first card: {computer_cards[0]}")
  
    if user_score == 0 or computer_score == 0 or user_score > 21:
      ret = True
    else:
      new = input("Type 'y' to get another card, type 'n' to pass:")
      if new == 'y':
        user_cards.append(deal_card())
      else:
        ret = True
          
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f"Your cards: {user_cards}, current score: {user_score}.")
  print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))

while input("Do you want to play a game of BlackJack? Type 'y' or 'n':") == 'y':
  play_game()
