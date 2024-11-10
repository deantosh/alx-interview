#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N non-attacking queens on an
N×N chessboard. Write a program that solves the N queens problem.

Usage: nqueens N
 - If the user called the program with the wrong number of arguments, print
   Usage: nqueens N, followed by a new line, and exit with the status 1
 - where N must be an integer greater or equal to 4
     - If N is not an integer, print N must be a number, followed by a new
       line, and exit with the status 1
     - If N is smaller than 4, print N must be at least 4, followed by a new
       line, and exit with the status 1
 - The program should print every possible solution to the problem
     - One solution per line
     - Format: see example
     - You don’t have to print the solutions in a specific order
 - You are only allowed to import the sys module
"""
import sys


import sys


def print_solution(board):
    """Helper function to print the solution in the required format"""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def is_safe(board, row, col):
    """Check if placing a queen at board[row][col] is safe"""
    for i in range(row):
        # Check for column conflict
        if board[i] == col:
            return False
        # Check for diagonal conflict
        if abs(board[i] - col) == abs(i - row):
            return False
    return True


def solve_nqueens(N, board, row):
    """Recursively solve the N Queens problem using backtracking"""
    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(N, board, row + 1)
            board[row] = -1  # Backtrack


def main():
    """Main function to handle input and call the solving function"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N  # Board initialized with -1 to represent empty columns
    solve_nqueens(N, board, 0)


if __name__ == "__main__":
    main()
