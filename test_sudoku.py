"""This module is to Test the Package"""

import sudoku

N = 9            # Dimension of the Grid
difficulty = 2      # Difficulty of the Puzzle ranges from ( 1 - 7 ) as 1 being the Lowest

obj = sudoku.Sudoku(N, difficulty)
matrix = obj.main()

# Custom Puzzle Check
custom_matrix = [       [1, 6, 7, 0, 9, 0, 0, 0, 0],
                        [0, 8, 3, 0, 5, 7, 0, 0, 2],
                        [9, 2, 5, 0, 8, 0, 6, 7, 3],
                        [8, 0, 0, 0, 4, 0, 3, 0, 9],
                        [0, 0, 2, 0, 0, 0, 0, 1, 6],
                        [3, 0, 0, 2, 1, 6, 8, 0, 0], 
                        [2, 9, 8, 1, 6, 4, 5, 0, 0], 
                        [7, 3, 0, 5, 0, 0, 9, 0, 4], 
                        [6, 0, 4, 0, 0, 3, 0, 8, 0]
                ]

def test_puzzle():
        assert obj.solver(matrix) == True

def test_custom_puzzle():
        assert obj.solver(custom_matrix) == True