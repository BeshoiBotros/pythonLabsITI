from abc import ABC, abstractclassmethod
import random
from typing import List

class Board:
    def __init__(self):
        self.__grid = [" "] * 9
    
    def display(self):
        print(self.__grid[0:3])
        print(self.__grid[3:6])
        print(self.__grid[6:9])

    def update(self, pos, symbol):
        if self.__grid[pos - 1] == " ":
            self.__grid[pos - 1] = symbol
            return True
        return False
    
    def check_winner(self, symbol):
        
        winning_table = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8], # columns
            [0, 4, 8], [2, 4, 6] # diagonals
        ]

        for combo in winning_table:
            winner = True
            for i in combo:
                if self.__grid[i] != symbol:
                    winner = False
                    break
            if winner:
                return True
        
        return False

    @property
    def grid(self):
        return self.__grid
    
    def get_available_positions(self):
        return [i + 1 for i, v in enumerate(self.__grid) if v == " "]
    
    def is_full(self):
        if " " not in self.__grid:
            return True
        return False
    
    def __str__(self):
        grid = self.__grid
        return f"""
                {grid[0]} | {grid[1]} | {grid[2]}
                ---+---+---
                {grid[3]} | {grid[4]} | {grid[5]}
                ---+---+---
                {grid[6]} | {grid[7]} | {grid[8]}
                """

class Player(ABC):
    
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    @abstractclassmethod
    def make_move(self, board):
        pass

class HumanPlayer(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol)
    
    def make_move(self, board: Board):
        
        while True:
            try:
                pos = int(input(f"{self.name}, {self.symbol} enter position (1-9): "))
                if pos < 1 or pos > 9:
                    print("Invalid Postion must be from 1-9")
                    continue

                if not board.update(pos, self.symbol):
                    print("This Pos already taken!")
                    continue
                break
            except:
                print("please Enter a valid integer number between (1-9)")

class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is making a move...")
        available = board.get_available_positions()
        pos = random.choice(available)
        board.update(pos, self.symbol)


class Game:

    def __init__(self, players: (HumanPlayer | ComputerPlayer)):
        self.players: List[HumanPlayer | ComputerPlayer] = players
        self.board: Board = Board()
        self.current_turn = 0
    
    def switch_turn(self):
        self. current_turn = 1 - self.current_turn
        return self.current_turn


    def play(self):
        print("game is started now >")

        while True:
            self.board.display()
            player = self.players[self.current_turn]
            player.make_move(self.board)
            if self.board.check_winner(player.symbol):
                print(f"{player.name} with symbol {player.symbol} is the winner")
                break
            
            if self.board.is_full():
                print("draw, no one winning!")
                break

            self.switch_turn()


