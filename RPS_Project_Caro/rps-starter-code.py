#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

#import the random module to create a move that will be able to return the moves at random
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""

class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass

#create a randomplayer as a subclass of player. The randomplayer returns one of 3 possible moves at random.
class RandomPlayer(Player):
    def move(self):
        print("in randomplayer")
        return random.choice(moves)

def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

        #create variables that will keep track of the scores
        self.p1_wins = 0
        self.p2_wins = 0
        self.ties = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            print('player1 wins')

            #increase the value of the variable that keep track of the wins of player 1
            self.p1_wins += 1
        elif move1 == move2:
            print('ties')
            #increase the value of the variable that keep track of the ties
            self.ties += 1
        else:
            print('player2 wins')

            #increase the value of the variable that keep track of the wins of player 2
            self.p2_wins += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        print("Game over!")

        #display the outcome of each round
        print(f" Player1 has won {self.p1_wins} times, Player 2 has won {self.p2_wins} times and there was/were {self.ties} ties")

if __name__ == '__main__':
    print("hoi")
    game = Game(RandomPlayer(), Player())
    game.play_game()
