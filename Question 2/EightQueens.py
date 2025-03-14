import random
import time


class EightQueens:
    def __init__(self):
        self.n = 8
        self.board = [random.randint(0, self.n - 1) for _ in range(self.n)]

    def get_conflicts(self):
        conflicts = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.board[i] == self.board[j] or abs(self.board[i] - self.board[j]) == j - i:
                    conflicts += 1
        return conflicts

    def hill_climbing(self, restart_count):
        min_conflicts = self.get_conflicts()
        restarts = 0
        moves = 0

        while min_conflicts > 0:
            for i in range(self.n):
                original_row = self.board[i]
                for j in range(self.n):
                    if j != original_row:
                        self.board[i] = j
                        conflicts = self.get_conflicts()
                        moves += 1
                        if conflicts < min_conflicts:
                            min_conflicts = conflicts
                            break
                else:
                    self.board[i] = original_row

            if min_conflicts == 0:
                break

            restarts += 1
            if restarts >= restart_count:
                break

            self.board = [random.randint(0, self.n - 1) for _ in range(self.n)]
            min_conflicts = self.get_conflicts()

        return moves, restarts


def main():
    results = []
    for _ in range(15):
        start_time = time.time()
        problem = EightQueens()
        moves, restarts = problem.hill_climbing(100)
        end_time = time.time()
        duration = (end_time - start_time) * 1000
        if problem.get_conflicts() == 0:
            print("Solution found: " + str(problem.board))
            solution = True
            results.append([moves, restarts, duration, solution])
        else:
            print("Solution not found.")
            solution = False
            results.append([moves, restarts, duration, solution])

    print("\nResults:\n")
    print(" Moves  Random Restarts  Duration (ms)  Solution")
    for moves, restarts, duration, solution in results:
        moves_str = str(moves).center(5)
        restarts_str = str(restarts).center(15)
        duration_str = "{:.6f}".format(duration).center(13)
        solution_str = str(solution).center(8)
        print(f"{moves_str}\t{restarts_str}\t{duration_str}\t{solution_str}")


if __name__ == "__main__":
    main()
