# game/player.py
class Player:
    def __init__(self, symbol):
        self.symbol = symbol

class HumanPlayer(Player):
    def get_move(self, board):
        while True:
            try:
                move = int(input(f"Player {self.symbol}, enter move (0-8): "))
                if move in board.get_available_moves():
                    return move
            except ValueError:
                pass
            print("Invalid move.")

class AIPlayer(Player):
    def __init__(self, symbol, ai_engine):
        super().__init__(symbol)
        self.ai_engine = ai_engine
    
    def get_move(self, board):
        return self.ai_engine.get_best_move(board)