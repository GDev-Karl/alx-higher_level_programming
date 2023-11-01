#!/usr/bin/python3
import sys

class NQueens:
    def __init__(self, N):
        self.N = N
        self.solutions = []

    def is_safe(self, board, row, col):
        for i in range(col):
            if board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False

        return True

    def print_solution(self, board):
        solution = []
        for i in range(self.N):
            for j in range(self.N):
                if board[i][j] == 1:
                    solution.append([i, j])
        self.solutions.append(solution)

    def solve(self):
        board = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.solve_helper(board, 0)

    def solve_helper(self, board, col):
        if col == self.N:
            self.print_solution(board)
            return

        for i in range(self.N):
            if self.is_safe(board, i, col):
                board[i][col] = 1
                self.solve_helper(board, col + 1)
                board[i][col] = 0

    def display_solutions(self):
        for solution in self.solutions:
            print(solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens.py N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    nqueens = NQueens(N)
    nqueens.solve()
    nqueens.display_solutions()
