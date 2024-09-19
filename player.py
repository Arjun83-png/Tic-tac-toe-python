# author: Arjun Taneja
# date: January 19, 2024
# file: player.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

from random import choice

class Player:
      def __init__(self, name, sign, board = None):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name
      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
            while True:
                cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                if cell in valid_choices:
                    if board.isempty(cell):
                        board.set(cell, self.sign)
                        break
                    else:
                        print('You did not choose correctly.')
                else:
                    print('You did not choose correctly.')

class AI(Player):
    def __init__(self, name, sign, board = None):
          super().__init__(name, sign)
        
    def choose(self,board):
        valid_choices = ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
        while True:
            cell = choice(valid_choices)
            if cell in valid_choices:
                    if board.isempty(cell):
                        board.set(cell, self.sign)
                        break
        print(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]: {cell}')

class MiniMax(AI):
    def __init__(self, name, sign, board = None):
        super().__init__(name, sign)
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self,board, True, True)
        print(cell)
        board.set(cell, self.sign)
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == '':
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
                
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
        
        if self.sign == 'X':
            opponent_sign = 'O'
        elif self.sign == 'O':
            opponent_sign = 'X'

        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        score = []
        move = []
        
        for cell in valid_choices:
            if board.isempty(cell):
                if self_player == True:
                    max_score = '-infinity'
                    board.set(cell,self.sign)
                    sco = self.minimax(board, False, False)
                    score.append(sco)
                    move.append(cell)
                    board.set(cell, ' ')
                else:
                    min_score = 'infinity'
                    board.set(cell,opponent_sign)
                    score.append(self.minimax(board, True, False))
                    move.append(cell)
                    board.set(cell, ' ')
                    
        # return the score / move
        max_score_index = score.index(max(score))
        print(score, move)
        if start:
            return move[max_score_index]
        return max(score) if self_player else min(score)
    
class SmartAI(AI):
    def __init__(self, name, sign, board = None):
        super().__init__(name, sign)
    def choose(self, board):
        print(f"\n{self.name}, {self.sign}: Enter a cell [A-C][1-3]: ")
        cell = MiniMax.minimax(self,board, True, True)
        print(cell)
        board.set(cell, self.sign)
    def minimax(self, board, self_player, start):
        # check the base conditions
        if board.isdone():
            # self is a winner
            if board.get_winner() == self.sign:
                return 1
            # is a tie
            elif board.get_winner() == '':
                return 0
            # self is a looser (opponent is a winner)
            else:
                return -1
                
        # make a move (choose a cell) recursively
        # use the pseudocode given to you above to implement the missing code
        
        if self.sign == 'X':
            opponent_sign = 'O'
        elif self.sign == 'O':
            opponent_sign = 'X'

        valid_choices = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
        score = []
        move = []
        
        for cell in valid_choices:
            if board.isempty(cell):
                if self_player == True:
                    max_score = '-infinity'
                    board.set(cell,self.sign)
                    sco = self.minimax(board, False, False)
                    score.append(sco)
                    move.append(cell)
                    board.set(cell, ' ')
                else:
                    min_score = 'infinity'
                    board.set(cell,opponent_sign)
                    score.append(self.minimax(board, True, False))
                    move.append(cell)
                    board.set(cell, ' ')
                    
        # return the score / move            
        max_score_index = score.index(max(score))
        if start:
            return move[max_score_index]
        return max(score) if self_player else min(score)
    
