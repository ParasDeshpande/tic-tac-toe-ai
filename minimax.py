class MinimaxAI:
    def __init__(self, player, opponent):
        self.player = player
        self.opponent = opponent
    
    def minimax(self, board, depth, is_maximizing):
        if board.is_winner(self.player):
            return 10 - depth
        if board.is_winner(self.opponent):
            return depth - 10
        if board.is_full():
            return 0
        
        if is_maximizing:
            best_score = -float('inf')
            for move in board.get_available_moves():
                board.make_move(move, self.player)
                score = self.minimax(board, depth + 1, False)
                board.board[move] = ' '
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for move in board.get_available_moves():
                board.make_move(move, self.opponent)
                score = self.minimax(board, depth + 1, True)
                board.board[move] = ' '
                best_score = min(score, best_score)
            return best_score
    
    def get_best_move(self, board):
        best_score = -float('inf')
        best_move = None
        for move in board.get_available_moves():
            board.make_move(move, self.player)
            score = self.minimax(board, 0, False)
            board.board[move] = ' '
            if score > best_score:
                best_score = score
                best_move = move
        return best_move