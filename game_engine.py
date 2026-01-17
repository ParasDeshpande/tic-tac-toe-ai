from game.board import Board
from ai.minimax import MinimaxAI

class TicTacToe:
    def __init__(self):
        self.board = Board()
        self.human = 'X'
        self.ai = 'O'
        self.ai_player = MinimaxAI(self.ai, self.human)
    
    def play(self):
        print("Welcome to Tic-Tac-Toe!")
        print("Positions are numbered 0-8:")
        print(" 0 | 1 | 2")
        print("---|---|---")
        print(" 3 | 4 | 5")
        print("---|---|---")
        print(" 6 | 7 | 8\n")
        
        while True:
            self.board.display()
            
            # Human turn
            while True:
                try:
                    move = int(input("Enter your move (0-8): "))
                    if move in self.board.get_available_moves():
                        self.board.make_move(move, self.human)
                        break
                    else:
                        print("Invalid move. Try again.")
                except ValueError:
                    print("Please enter a number.")
            
            if self.board.is_winner(self.human):
                self.board.display()
                print("You win!")
                break
            
            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break
            
            # AI turn
            print("AI is thinking...")
            ai_move = self.ai_player.get_best_move(self.board)
            self.board.make_move(ai_move, self.ai)
            print(f"AI plays position {ai_move}")
            
            if self.board.is_winner(self.ai):
                self.board.display()
                print("AI wins!")
                break
            
            if self.board.is_full():
                self.board.display()
                print("It's a tie!")
                break