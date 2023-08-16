from sudoku import Sudoku

# Create a new Sudoku puzzle with a difficulty level of 0.7
puzzle = Sudoku(3).difficulty(0.5)

# Display the puzzle
print("Sudoku Puzzle:")
puzzle.show()

# Display the solution
print("\nSolution:")
puzzle.solve()
