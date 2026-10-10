"""Sudoku solver implementation with backtracking."""

SQUARE_SIZE = 3


def is_valid(board):
    """Check if the board is valid (no conflicts)."""
    for row in board:
        if len(set(row)) != 9:
            return False
    for col in range(9):
        if len(set(board[row][col] for row in range(9))) != 9:
            return False
    for box_row in range(0, 9, 3):
        for box_col in range(0, 9, 3):
            box = []
            for r in range(box_row, box_row + 3):
                for c in range(box_col, box_col + 3):
                    box.append(board[r][c])
            if len(set(box)) != 9:
                return False
    return True


def is_empty(board, row, col):
    """Check if a cell is empty (0)."""
    return board[row][col] == 0


def get_candidates(board, row, col):
    """Get valid candidates for a cell."""
    candidates = set(range(1, 10))
    
    # Exclude values in row
    for c in range(9):
        candidates.discard(board[row][c])
    
    # Exclude values in column
    for r in range(9):
        candidates.discard(board[r][col])
    
    # Exclude values in 3x3 box
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(box_row, box_row + 3):
        for c in range(box_col, box_col + 3):
            candidates.discard(board[r][c])
    
    return list(candidates)


def solve(board):
    """Solve the Sudoku using backtracking. Returns the solved board or None."""
    for row in range(9):
        for col in range(9):
            if is_empty(board, row, col):
                candidates = get_candidates(board, row, col)
                for candidate in candidates:
                    board[row][col] = candidate
                    if solve(board):
                        return board
                    board[row][col] = 0
                return None
    return board


class Sudoku:
    """Sudoku board wrapper with validation and solving."""
    
    def __init__(self, board):
        """Initialize with a 9x9 board."""
        self._board = [list(row) for row in board]
        if not is_valid(self._board):
            raise ValueError("Invalid board provided")
    
    @property
    def board(self):
        """Return a copy of the board."""
        return [row[:] for row in self._board]
    
    def solve(self):
        """Solve the board and return the solved board."""
        solved = solve(self._board)
        if solved is None:
            return None
        self._board = solved
        return self.board
    
    def is_valid(self):
        """Check if the current board is valid."""
        return is_valid(self._board)
    
    def is_empty(self, row, col):
        """Check if a cell is empty."""
        return is_empty(self._board, row, col)
    
    def get_candidates(self, row, col):
        """Get valid candidates for a cell."""
        return get_candidates(self._board, row, col)
