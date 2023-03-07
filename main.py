############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo
from replit import clear


def deal_card():
  """returns a random card from the given list"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)

def calculate_score(cards):
  #"""returns the score for given card list"""
  score = sum(cards)
  #for 2 cards deck check for blackjack ace(11) and 10 , return     0 if blackjack
  if score == 21 and len(cards) == 2:
      return 0
    #if sum > 21 and deck has 11 change it to 1
  if 11 in cards and score > 21:
      cards.remove(11)
      cards.append(1)
      score = sum(cards)

  return score

def compare(user_score, computer_score):
  """compare user and computer score to decide  the result"""
  if user_score == computer_score:
      return "Draw"
  elif user_score == 0:
      return "User wins with a blackjack"
  elif computer_score == 0:
      return "Computer wins with a blackjack"
  elif user_score > 21:
      return "User score went over , Computer wins"
  elif computer_score > 21:
      return "Computer score went over , User wins"
  elif user_score > computer_score:
      return "User wins"
  else:
      return "Computer wins"

def play_blackjack():
  print(logo)
  user_cards = []
  computer_cards = []

  end_of_game = False

  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not end_of_game:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"User hand: {user_cards} , User score {user_score}")
    print(f"Computer first card {computer_cards[0]}, computer score {computer_score}")
        
    if user_score == 0 or computer_score == 0 or user_score > 21:
      end_of_game = True
    else:
      user_draw_another = input("Do you want to draw another card? y or n: ").lower()
      if user_draw_another == 'y':
        user_cards.append(deal_card())
      else:
        end_of_game = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f" User final score: {user_score} User hand {user_cards}")
  print(f" Computer final score: {computer_score} Computer hand: {computer_cards}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of blackjack y or n? ").lower() == 'y':
    clear()
    play_blackjack()
else:
    print("Thanks for playing....")