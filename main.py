import random #hint
from blackjack_art import logo #Game logo
#Create  a deck of cards
def deck():
   cards = [2,3,4,5,6,7,8,9,10,"Ace","Jack","King","Queen"]
   category = ["♠️","♥️ ","♦️","♣️"]
   pile = []

   for card in cards:
      for i in category:
         pile.append((i,card))

   return pile

pile = deck()
# print(pile)
def deal():
   random.shuffle(pile)
   random.shuffle(pile)
   random.shuffle(pile)

   player1 = []
   player2 = []

   for i in range(8):
      player1.append(pile.pop())
      player2.append(pile.pop())

   return player1

print(deal())


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