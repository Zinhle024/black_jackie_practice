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

value = hand_value



def play(p1,com):
   while True:
      print(f"\nYour hand value is {hand_value(p1)}\n")
      print(f"Computer's hand: {com} (Value: {hand_value(com)})")

      P1_choice = input("Player1 - Hit or Stand? ") 

      if P1_choice.lower().strip() == "stand":
         break

      if P1_choice.lower().strip() == "hit":
         p1.append(pile.pop())

      while P1_choice.lower().strip() != "stand" and P1_choice.lower().strip() != "hit":
         P1_choice = input("Please entre valid input:")

      if "Ace" in p1[0] or "Ace" in p1[1]:
         if hand_value(p1) > 12:
            value + 1
         else:
            value + 11
         print("WOOOOW")

      if hand_value(player1) > 21:
         print("YOU BUST!")
         break

      if hand_value(com) < 17:
         computor.append(pile.pop())


   


   return (f"Player1 = {p1},Computor = {com}")

plays = play(player1,computor)
   
# print(plays)

def winner():
   # index = [0,1]
   # results = []
   # for i in index:
   #    if  any player1[index] == "Ace" and isinstance(player1[index],str) or  player1[index] == 10:
   #    print(f"\nYOU - BLACKJACK!!! \n")
   if player1[0] == "Ace" and type(player1[1]) == str or  player1[1] == 10:
      print(f"\nYOU - BLACKJACK!!! \n")
   if hand_value(computor) == 21 and len(computor) == 2:
      print(f"\nCOMPUTOR - BLACKJACK!!! \n")
   if hand_value(player1) > hand_value(computor) and hand_value(player1) < 21:
      print(f"\nYOU WIN!! \n")
   if hand_value(player1) < hand_value(computor):
         print(f"\nYOU LOSE ")
   if hand_value(player1) == hand_value(computor):
         print(f"\nPUSH ")


winner()
      
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
