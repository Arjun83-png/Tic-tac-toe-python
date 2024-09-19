# author: Arjun Taneja
# date: January 19, 2024
# file: board.py a Python program that implements a tic-tac-toe game
# input: user responses (strings)
# output: interactive text messages and a tic-tac-toe board

class Board:
      def __init__(self):
            # board is a list of cells that are represented 
            # by strings (" ", "O", and "X")
            # initially it is made of empty cells represented 
            # by " " strings
            self.sign = " "
            self.size = 3
            self.board = list(self.sign * self.size**2)
            # the winner's sign O or X
            self.winner = ""
            
      def get_size(self):
            # optional, return the board size (an instance size)
            return self.size
        
      def get_winner(self):
            # return the winner's sign O or X (an instance winner)
            if self.board[0] == self.board[1] == self.board[2] == 'X' != ' ' or self.board[3] == self.board[4] == self.board[5] == 'X' != ' ' or self.board[6] == self.board[7] == self.board[8] == 'X' != ' ' or self.board[0] == self.board[4] == self.board[8] == 'X' != ' ' or self.board[6] == self.board[4] == self.board[2] == 'X' != ' ' or self.board[0] == self.board[3] == self.board[6] == 'X' != ' ' or self.board[1] == self.board[4] == self.board[7] == 'X' != ' ' or self.board[2] == self.board[5] == self.board[8] == 'X' != ' ':
                  self.winner = 'X'
            elif self.board[0] == self.board[1] == self.board[2] == 'O' != ' ' or self.board[3] == self.board[4] == self.board[5] == 'O' != ' ' or self.board[6] == self.board[7] == self.board[8] == 'O' != ' ' or self.board[0] == self.board[4] == self.board[8] == 'O' != ' ' or self.board[6] == self.board[4] == self.board[2] == 'O' != ' ' or self.board[0] == self.board[3] == self.board[6] == 'O' != ' ' or self.board[1] == self.board[4] == self.board[7] == 'O' != ' ' or self.board[2] == self.board[5] == self.board[8] == 'O' != ' ':
                  self.winner = 'O'
            
            return self.winner
        
      def set(self, cell, sign):
            # mark the cell on the board with the sign X or O
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # you can use a tuple ("A1", "B1",...) to obtain indexes 
            # this implementation is up to you
            valid_choices = ["A1", "B1", "C1", "A2","B2","C2","A3","B3","C3"]
            self.board[valid_choices.index(cell)] = sign
            
      def isempty(self, cell):
            # you need to convert A1, B1, …, C3 cells into index values from 1 to 9
            # return True if the cell is empty (not marked with X or O)
            valid_choices = ["A1", "B1", "C1", "A2","B2","C2","A3","B3","C3"]
            if self.board[valid_choices.index(cell)] != 'X' and self.board[valid_choices.index(cell)] != 'O':
                  return True
            else:
                  return False
            
            
      def isdone(self):
            done = False
            self.winner = ''
            # check all game terminating conditions, if one of them is present, assign the var done to True
            # depending on conditions assign the instance var winner to O or X
            ## Convert to loop 
            if self.board[0] == self.board[1] == self.board[2] != ' ' or self.board[3] == self.board[4] == self.board[5] != ' ' or self.board[6] == self.board[7] == self.board[8] != ' ' or self.board[0] == self.board[4] == self.board[8] != ' ' or self.board[6] == self.board[4] == self.board[2] != ' ' or self.board[0] == self.board[3] == self.board[6] != ' ' or self.board[1] == self.board[4] == self.board[7] != ' ' or self.board[2] == self.board[5] == self.board[8] != ' ' or " " not in self.board:
                  done = True
            return done
      
      def show(self):
            # draw the board
            l = [(2,2),(2,6),(2,10),(4,2),(4,6),(4,10),(6,2),(6,6),(6,10)]
            print(f'   A   B   C ')
            for column in range(1,8):
                if column % 2 == 0:
                   print('{}|'.format(int(column / 2)),end = '')
                   
                   for elem in range(1,13):
                      if elem % 4 == 0 and elem != 12:
                            print('|',end = '')
                      elif (column,elem) in l:
                            print(self.board[l.index((column,elem))],end = '')
                      elif elem % 4 != 0:
                            print(" ",end = '')
                      elif elem % 4 == 0 and elem == 12:
                            print('|')
            
                            
                else:
                    print(' +',end = '')
                    for row in range(1,13):
                        if row % 4 == 0 and row != 12:
                            print('+',end = '')
                        elif row == 12:
                            print('+')
                        else:
                            print('-',end = '')     
