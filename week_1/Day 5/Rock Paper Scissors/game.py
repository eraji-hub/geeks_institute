# game.py
import random

class Game:
    def get_user_item(self):
        """Ask the user to select rock, paper, or scissors"""
        choices = ['r', 'p', 's']
        while True:
            user_item = input("Select (r)ock, (p)aper, or (s)cissors: ").lower()
            if user_item in choices:
                return user_item
            else:
                print("Invalid choice. Please try again.")

    def get_computer_item(self):
        """Randomly select rock, paper, or scissors for computer"""
        choices = ['r', 'p', 's']
        return random.choice(choices)

    def get_game_result(self, user_item, computer_item):
        """Determine the result of the game"""
        if user_item == computer_item:
            return 'draw'
        elif (user_item == 'r' and computer_item == 's') or \
             (user_item == 'p' and computer_item == 'r') or \
             (user_item == 's' and computer_item == 'p'):
            return 'win'
        else:
            return 'loss'

    def play(self):
        """Play a single round"""
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)

        # تحويل الحروف للاسم الكامل لعرضه
        names = {'r': 'rock', 'p': 'paper', 's': 'scissors'}
        print(f"You selected {names[user_item]}. The computer selected {names[computer_item]}. Result: {result}")

        return result
