'''
Create a Tic Tac Toe game in python.
1. You should be able to play with two players.
2. You should be able to play against computer.
After you complete simple game implement it in a way that computer never loses.
'''

import random

class GameBoard:
    winning_positions = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    def __init__(self):
        self.board_position = [' '] * 9

    def print_board(self):
        for i in range(3):
            row = self.board_position[i*3:(i+1)*3]
            print(' ' + ' | '.join(row))
            if i < 2:
                print('---+---+---')
        print()

    def update_position(self, position, sign):
        if self.board_position[position] == ' ':
            self.board_position[position] = sign
            return True
        return False
  
    def check_winner(self, sign):
        for position in GameBoard.winning_positions:
            if all(self.board_position[i] == sign for i in position):
                return True
        return False

    def is_board_full(self):
        return ' ' not in self.board_position


class Player:
    def __init__(self, sign):
        self.sign = sign

    def make_player_move(self, board):
        try:
            player_move = int(input(f"Player {self.sign}'s player_move (1-9): ")) - 1
            return player_move
        except ValueError:
            return -1


class Computer(Player):
    def make_player_move(self, game_board):
        available_positions = [i for i in range(9) if game_board.board_position[i] == ' ']
        computer_choice = random.choice(available_positions)
        return computer_choice


class StartGame:
    def __init__(self):
        self.game_board = GameBoard()
        self.player1 = Player('X')
        self.player2 = None
        self.current_player = self.player1

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def play(self):
        while True:
            self.game_board.print_board()

            player_move = self.current_player.make_player_move(self.game_board)

            if player_move < 0 or player_move > 8:
                print("Invalid player_move! Try again.\n")
                continue

            if not self.game_board.update_position(player_move, self.current_player.sign):
                print("Position already taken! Try again.\n")
                continue

            if self.game_board.check_winner(self.current_player.sign):
                self.game_board.print_board()
                if isinstance(self.current_player, Computer):
                    print("Computer Wins!")
                else:
                    print(f"Player {self.current_player.sign} Wins!")
                break

            if self.game_board.is_board_full():
                self.game_board.print_board()
                print("Match Draw!")
                break

            self.switch_player()

    def start_game(self):
        print("---- Tic Tac Toe ----")
        print('\n1.With 2 Player\n2.With Computer')
        choose_game = input('\nEnter Choice: ')

        if choose_game == '1':
            self.player2 = Player('O')
            self.current_player = self.player1
            self.play()

        elif choose_game == '2':
            self.player2 = Computer('O')
            self.current_player = self.player1
            self.play()

        else:
            print('Invalid Choice')

tt = StartGame()
tt.start_game()