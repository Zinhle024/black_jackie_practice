import random #hint
from blackjack_art import logo #Game logo
#Create  a deck of cards
def deck():
   cards = [2,3,4,5,6,7,8,9,10,"Ace","Jack","King","Queen"]
   category = ["♠️","♥️ ","♦️","♣️"]
   pile = []

   for card in cards:
      for i in category:
         pile.append((card,i))

   return  pile

pile = deck()


def deal():
   random.shuffle(pile)
   random.shuffle(pile)
   random.shuffle(pile)

   player1 = []
   computor = []

   for i in range(2):
      player1.append(pile.pop())
      computor.append(pile.pop())
      

   print(f"Player1 = {player1} \n\nComputor = {computor}\n")
   return player1,computor

players = deal()
player1 = players[0]
computor = players[1]



def hand_value(hand):
   value = 0
   for i in hand:
      if type(i[0]) == str and i[0] != "Ace":
         value += 10
      elif type(i[0]) == int:
         value += i[0]
   return value

def play(p1,com):
   if hand_value(p1) > 21 or hand_value(com)> 21:
      True
   while True:
      P1_choice = input("Player1 - Hit or Stand? ")
      if P1_choice.lower().strip() == "hit":
         p1.append(pile.pop())
   
      if P1_choice.lower().strip() == "stand":

         return hand_value(p1)
   
      print(hand_value(p1))
      if hand_value(p1) < 21:
         P1_choice = input("Player1 - Hit or Stand? ")
         
      return p1
print(play(player1,computor))




def main():
    """
TODO: Blackjack Game Implementation

This module will simulate a simplified version of a Blackjack card game.

Features to Implement:
1. Game Setup:
   - Create a deck of 52 cards (without jokers) using standard suits and ranks.
   - Shuffle the deck before dealing cards.

2. Player and Dealer Setup:
   - Implement player and dealer hands.
   - Each hand should be able to hold cards and calculate its total value.
   - Aces can count as either 1 or 11, depending on the hand's value.

3. Game Flow:
   - Deal two cards to both the player and the dealer.
   - Allow the player to "hit" (get another card) or "stand" (stop drawing cards).
   - Dealer should follow the standard rules (e.g., hit until reaching 17 or higher).

4. Determine Outcomes:
   - Implement the winning conditions:
     - Player or dealer gets Blackjack (21 points with two cards).
     - Player or dealer busts (exceeds 21 points).
     - Player's hand is closer to 21 than the dealer's hand without going over.
   - Implement conditions for a push (tie).

5. User Interface:
   - CLI interface for the game.
   - Display the player's hand, dealer's visible card, and game status.
   - Announce the winner at the end of each game.


7. Code Optimizations and Error Handling:(BONUS NOT A MUST !!!)
   - Add input validation for player choices (hit or stand).
   - Handle edge cases (e.g., deck running out of cards).
   - Ensure proper game loop for continuous play.

"""