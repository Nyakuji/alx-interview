#!/usr/bin/python3
"""N queens puzzle"""
import sys

# Validate the command-line arguments
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    sys.exit(1)

if not sys.argv[1].isdigit():
    print("N must be a number")
    sys.exit(1)

n = int(sys.argv[1])
if n < 4:
    print("N must be at least 4")
    sys.exit(1)


def queens(n, i=0, a=[], b=[], c=[]):
    """
    Generate all possible solutions for the N queens puzzle.

    This is a recursive generator function that yields solutions
    as they are found.

    Args:
        n: The size of the chessboard and the number of queens to place.
        i: The current index of the row to place a queen.
        a: A list of columns where queens are already placed.
        b: A list of diagonals (from top-left to bottom-right)
          already occupied by queens.
        c: A list of diagonals (from top-right to bottom-left)
           already occupied by queens.

    Yields:
        A list representing the positions of N queens on the chessboard.
    """
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def solve(n):
    """
    Solve the N queens puzzle and print all possible solutions.

    Args:
        n: The size of the chessboard and the number of queens to place.

    Returns:
        None
    """
    for solution in queens(n):
        solution_list = [[i, j] for i, j in enumerate(solution)]
        print(solution_list)


# Execute the solve function if the script is run directly
if __name__ == "__main__":
    solve(n)
