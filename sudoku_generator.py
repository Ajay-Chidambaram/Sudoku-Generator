"""sudoku_generator.py: Program to Generate a Sudoku Puzzle of Unique Solution"""

__author__      = "Chidambaram"

from random import randint, shuffle
import math


no_of_solutions = 1

# Function to Check the cell which consists of three sub-functions
def check_if_safe(matrix, i, j, num):
    """
    This Functions Helps to check whether the given num is already exits or not

    This function uses another three sub-functions
    
    -> unUsed_in_box : helps to check num exists or not within its square matrix
    -> unUsed_in_row : helps to check num exists or not in the respective row
    -> unUsed_in_col : helps to check num exists or not in the respective column

    Args:
        matrix ([2D List]): It is the actual Sudoku Grid which is in the form of 2D List
        i ([int]): It describes the Row Number
        j ([int]): It describes the Column Number
        num ([int]): It is the Element which have to be check whether it can present in the 
                particular cell of the grid

    Returns:
        [boolean]: It returns TRUE in case of num doesn't exist in the respective
                row, column and the inner square matrix else it return FALSE
    """
    return (unUsed_in_row(matrix, i, num) and unUsed_in_col(matrix, j, num) and unUsed_in_box(matrix, i-i%SRN, j-j%SRN, num))

# Sub-Function 1 to check whether same num present in the square box
def unUsed_in_box(matrix, row, col, num):
    for i in range(SRN):
        for j in range(SRN):
            if matrix[row + i][col + j] == num:
                return False

    return True

# Sub-Function 2 to check whether same num present in that row
def unUsed_in_row(matrix, row, num):
    for j in range(N):
        if matrix[row][j] == num:
            return False
    return True

# Sub-Function 3 to check whether same num present in that column
def unUsed_in_col(matrix, col, num):
    for i in range(N):
        if matrix[i][col] == num:
            return False
    return True

# Function to check every cell in the grid for the occurence of Zero
# If it has Zero, it returns FALSE else TRUE
def check_grid(grid):
  for row in range(0,N):
      for col in range(0,N):
        if grid[row][col]==0:
          return False

  #We have a complete grid!  
  return True 

'''
def solve_grid_utility(matrix, row, col):
    if matrix[row][col] == 0:
        for num in range(1, N+1):
            if check_if_safe(matrix, row, col, num):
                return num
        
    return -1
'''

def solve_grid(matrix):
    global no_of_solutions
    for i in range(0, N*N):
        row = i // N
        col = i % N
        '''
        num = solve_grid_utility(matrix, row, col)
        
        if num > 0:
            matrix[row][col] = num
            if check_grid(matrix):
                no_of_solutions += 1
                break
            else:
                if solve_grid(matrix):
                    return True

        '''
        if matrix[row][col] == 0:
            for num in range(1, N+1):
                if check_if_safe(matrix, row, col, num):
                    matrix[row][col] = num
                    if check_grid(matrix):
                        no_of_solutions = no_of_solutions + 1
                        break
                    else:
                        if solve_grid(matrix):
                            return True

            break
        
    matrix[row][col] = 0


def fill_grid(matrix):
    """Function to fill the N x N Grid with constraints

    Args:
        matrix ([2D List]): It is the actual Sudoku Grid which is in the form of 2D List

    Returns:
        [boolean]: If the Grid is fully filled then it returns TRUE
                else returns FALSE

    Algorithm:
        1] Choose a cell which is not filled yet 
        2] Check a random number can able to accomodate in that cell with respect to constraints
        3] If yes, recursively call the function to fill further cells
        4] If not, backtrack to previous stage and choose another random number  
    """
    for i in range(0,N*N):
        row = i // N
        col = i % N

        if matrix[row][col] == 0:
            shuffle(numberList)
            for num in numberList:
                if check_if_safe(matrix, row, col, num):
                    matrix[row][col] = num
                    if check_grid(matrix):
                        return True
                    else:
                        if fill_grid(matrix):
                            return True

            break

    matrix[row][col] = 0


def remove_cells(matrix, attempts):
    """This Function helps to Remove elements in the grid in order to make it as Puzzle

    Args:
        matrix ([2D List]): It is the actual Sudoku Grid which is in the form of 2D List
        attempts ([int]): It describes the difficulty of the Puzzle 
    """
    global no_of_solutions
    while attempts > 0 :
        row = randint(0, N-1)
        col = randint(0, N-1)
        while matrix[row][col] == 0:
            row = randint(0, N-1)
            col = randint(0, N-1)

        cell_backup = matrix[row][col]
        matrix[row][col] = 0

        no_of_solutions = 0
        copy_matrix = [each_row[:]for each_row in matrix]
        solve_grid(copy_matrix)

        # print("@@ Number of Solutions ", no_of_solutions)
        # print_matrix(copy_matrix)
        # print("@@ Attempts ", attempts)

        # It is to check at the different stages the puzzle has unique solution
        if no_of_solutions != 1:
            # if not reinsert the removed cell
            matrix[row][col] = cell_backup
            attempts = attempts - 1


# Function to print the Sudoku Grid 
def print_matrix(matrix):
    print(" --" + "--"*(N) + "--")
    for row in range(N):
        for col in range(N):
            if col % SRN == 0:
                print("| " + str(matrix[row][col]), end=" ")
            elif col == N - 1:
                print(str(matrix[row][col]) + "|", end=" ")
            else:
                print(str(matrix[row][col]), end=" ")
        
        if (row + 1) % SRN == 0:
            print(end="\n")
            print(" --" + "--"*(N) + "--")
        else:
            print()


def main():
    """Main Function

    The steps invloved in the main function are :

    1] Getting N as Input inorder to make N x N Grid
    2] Initializing a 2D Grid of N x N size with zeros
    3] Fill the grid with values using fill_grid()
    4] Removing elements in that Grid to make it as puzzle using remove_cells() 
    """
    global N, SRN, numberList

    N = int(input("Enter N value : "))
    SRN = int((math.sqrt(N)))                             # User Input
    matrix = [[0 for i in range(N)]for j in range(N)]     # empty grid
    numberList = list(range(1, N+1))                      # numbers should be in the grid

    print("\n\nActual Solution \n")
    fill_grid(matrix)
    print_matrix(matrix)

    print("\n\nFinal Result \n")
    remove_cells(matrix, 2)
    print_matrix(matrix)


if __name__ == "__main__":
    main()