# Challenge: Playing Rock-Paper-Scissors!
# Try your hand at writing a rock-paper-scissors game in Python
from numpy import random

choices = ['rock', 'paper', 'scissors']

p1 = random.choice(choices)
p2 = random.choice(choices)

class game():
    
    def __init__(self, p1, p2):
        
        self.p1 = p1
        self.p2 = p2
        
    
    def play(self):
        
        if self.p1 == self.p2:
            print('tie')
            
        elif (self.p1 == 'rock' and self.p2 == 'scissors') or (self.p1 == 'paper' and self.p2 == 'rock') or (self.p1 == 'scissors' and self.p2 == 'paper'):
            print('Player 1 got {}, player 2 got{}'.format(self.p1, self.p2))
            print('Player 1 wins!')
        
        else:
            print('Player 1 got {}, player 2 got {}'.format(self.p1, self.p2))
            print('Player 2 wins!')

game1 = game(p1, p2)
game1.play()
