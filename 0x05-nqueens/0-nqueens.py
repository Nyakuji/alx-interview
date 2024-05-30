#!/usr/bin/python3
"""N queens problem"""
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at board[row][col].

    This function checks for a queen's safety by
    ensuring there are no other queens
    in the same row, column, or diagonals.

    Args:
        board: A 2D list representing the chessboard.
        row: The current row to check.
        col: The current column to check.
        n: The size of the chessboard.

    Returns:
        A boolean value indicating if the position is safe.
    """
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens(board, col, n):
    """Solve the N queens problem by placing queens on the chessboard.

    This function places queens one by one in different columns,
    starting from the leftmost column.

    Args:
        board: A 2D list representing the chessboard.
        col: The current column to place a queen.
        n: The size of the chessboard.

    Returns:
        None
    """
    # base case: If all queens are placed
    if col >= n:
        print_solution(board, n)
        return

    # Consider this column and try placing this queen in all rows one by one
    for i in range(n):
        if is_safe(board, i, col, n):
            # Place this queen in board[i][col]
            board[i][col] = 1

            # recur to place rest of the queens
            solve_n_queens(board, col + 1, n)

            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove queen from board[i][col]
            board[i][col] = 0  # backtrack


def print_solution(board, n):
    """Print the chessboard with queens placed.

    This function prints the solution of the N queens problem.

    Args:
        board: A 2D list representing the chessboard with queens placed.
        n: The size of the chessboard.

    Returns:
        None
    """
    solution = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                solution.append([i, j])
    print(solution)


if __name__ == "__main__":
    # Check for the correct number of command-line arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Check if the provided argument is an integer and at least 4
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Initialize the board and solve the problem
    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0, N)
