"""Sudoku Puzzle Generator

Program to Generate a Sudoku Puzzle which has Unique Solution

Algorithm:
            1] Choose a cell which is not filled yet 
            2] Check a random number can able to accomodate in that cell with respect to constraints
            3] If yes, recursively call the function to fill further cells
            4] If not, backtrack to previous stage and choose another random number
"""

from random import randint, shuffle
import math

class Sudoku:
    """Sudoku Class

    Main Attributes are ,
        1] N [int] : It describes the dimension of the Grid
        2] difficulty [int] : It describes the difficulty of the Puzzle ranges from ( 1 - 7 ) as 1 being the Lowest
        3] matrix [2D list] : Program generated 2D List initially consists of 0's
        4] number_list [list] : List of numbers that should be in the grid
        5] no_of_solutions [int] : It describes the Unique solution of the puzzle
    """
    def __init__(self, N, difficulty):
        self.N = N                        # N is the Dimension of the grid (N x N)
        self.SRN = int(math.sqrt(N))      # Square Root of N
        self.difficulty = difficulty      # From 1 to 7 as 1 being the Lowest
        self.matrix = [[0 for i in range(self.N)] for j in range(self.N)]
        self.number_list = list(range(1, self.N + 1))
        self.no_of_solutions = 1

    def main(self):
        self.__fill_grid(self.matrix)
        self.print_matrix()
        print("\n\nPuzzle\n")
        self.__remove_cells()
        self.print_matrix()

        return self.matrix
        
    def __is_safe(self, row, col, matrix, num):
        """Check whether the num can be placed in the respective row and col index

        Args:
            row ([int]): It descibes the Row index
            col ([int]): It descibes the Column index
            matrix ([2D list]): N x N sudoku Grid 
            num ([int]): number to be check which can be placed or not

        Returns:
            [boolean]: If num can be placed in that cell it returns TRUE else it
                    returns FALSE
        """

        # Check whether num is already present in that Column
        for j in range(self.N):
            if matrix[row][j] == num:
                return False

        # Check whether num is already present in that Row
        for i in range(self.N):
            if matrix[i][col] == num:
                return False

        # # Check whether num is already present in the inner square matrix
        row = row - row % self.SRN
        col = col - col % self.SRN

        for i in range(self.SRN):
            for j in range(self.SRN):
                if matrix[row + i][col + j] == num:
                    return False

        return True

    def __check_grid(self, matrix):
        """AI is creating summary for __check_grid

        Args:
            matrix ([2D list]):  N x N sudoku Grid

        Returns:
            [tuple]: If the zero is exists in that grid it returns (row, col) of that cell
                else it returns (-1, -1) to show there is no 0's in the grid
        """

        for i in range(self.N):
            for j in range(self.N):
                if matrix[i][j] == 0:
                    return (i, j)       # It Zero occurs return its row and col index
        
        # It shows the grid has no zeros
        return (-1, -1)
    
    def __fill_grid(self, matrix):
        """Recursive Function to Fill the Empty Grid with Values"""

        row, col = self.__check_grid(matrix)

        if row == -1 and col == -1:
            return True

        shuffle(self.number_list)

        for num in self.number_list:
            if self.__is_safe(row, col, matrix, num):
                matrix[row][col] = num
                if self.__check_grid(matrix) == (-1, -1):
                    return True
                
                if self.__fill_grid(matrix):
                    return True
                
        
        matrix[row][col] = 0


    def solve_grid(self, matrix):
        """Recursive Function to Solve the Grid with Values"""
        
        row, col = self.__check_grid(matrix)
        
        if row == -1 and col == -1:
            return True

        for num in range(1, self.N + 1):
            if self.__is_safe(row, col, matrix, num):
                matrix[row][col] = num
                if self.__check_grid(matrix) == (-1, -1):
                    self.no_of_solutions += 1
                    break
                
                if self.solve_grid(matrix):
                    return True

        matrix[row][col] = 0
        

    def __remove_cells(self):
        """Function to get a Puzzle from a fully filled grid"""

        while self.difficulty > 0:
            row = randint(0, self.N - 1)
            col = randint(0, self.N - 1)

            # If the above choosed cell has 0 in it choose different cell
            while self.matrix[row][col] == 0:
                row = randint(0, self.N - 1)
                col = randint(0, self.N - 1)

            cell_backup = self.matrix[row][col]
            self.matrix[row][col] = 0

            self.no_of_solutions = 0
            copied_matrix = [each_row[:]for each_row in self.matrix]
            print(self.solve_grid(copied_matrix))

            # If the Puzzle has more than one Solution replace the 
            # last taken cell value in that 
            if self.no_of_solutions != 1:
                self.matrix[row][col] = cell_backup
                self.difficulty -= 1


    def solver(self, matrix):
        """Function to check Custom Sudoku Puzzles From the User

        Args:
            matrix ([2D list]):  N x N sudoku Grid

        Returns:
            [boolean]: If the puzzle is solvable and it has a single solution, it
                    returns TRUE else it returns FALSE
        """

        row, col = self.__check_grid(matrix)

        if row == -1 and col == -1:
            return True
        
        self.no_of_solutions = 0
        self.solve_grid(matrix)

        if self.no_of_solutions != 1:
            return False
        
        return True


    # Function to print the Sudoku Grid 
    def print_matrix(self):
       
        no_of_zeros = 0
        print(" --" + "--"*(self.N) + "--")
        for row in range(self.N):
            for col in range(self.N):

                element = str(self.matrix[row][col])
                
                if element == "0": 
                    no_of_zeros += 1

                if col % self.SRN == 0:
                    print("| " + element, end=" ")
                elif col == self.N - 1:
                    print(element + "|", end=" ")
                else:
                    print(element, end=" ")
            
            if (row + 1) % self.SRN == 0:
                print("\n --" + "--"*(self.N) + "--")
            else:
                print()

            
        if no_of_zeros != 0:
            print("Number of Cells Removed : ", no_of_zeros)


if __name__ == "__main__":

    N = 9            # Dimension of the Grid
    difficulty = 2      # Difficulty of the Puzzle ranges from ( 1 - 7 ) as 1 being the Lowest
    obj = Sudoku(N, difficulty)
    obj.main()