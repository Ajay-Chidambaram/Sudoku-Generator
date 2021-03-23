from random import randint, shuffle
import math


def check_if_safe(matrix, i, j, num):
    return (unUsed_in_row(matrix, i, num) and unUsed_in_col(matrix, j, num) and unUsed_in_box(matrix, i-i%SRN, j-j%SRN, num))

def unUsed_in_box(matrix, row, col, num):
    for i in range(SRN):
        for j in range(SRN):
            if matrix[row + i][col + j] == num:
                return False

    return True

def unUsed_in_row(matrix, row, num):
    for j in range(N):
        if matrix[row][j] == num:
            return False
    return True

def unUsed_in_col(matrix, col, num):
    for i in range(N):
        if matrix[i][col] == num:
            return False
    return True

def check_grid(grid):
  for row in range(0,N):
      for col in range(0,N):
        if grid[row][col]==0:
          return False

  #We have a complete grid!  
  return True 

def fill_grid(matrix):

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

def remove_k_cells(matrix, num_of_cells):
    
    for k in range(num_of_cells):
        
        while True:
            cell = randint(0, (N*N)-1)
            row = cell // N
            col = cell % N

            if matrix[row][col] != 0:
                matrix[row][col] = 0
                break;
            else:
                continue
    
def print_matrix(matrix):
    for row in matrix:
        print(row)


def main():
    global N, SRN, numberList
    N = int(input("Enter N value : "))
    SRN = int(math.sqrt(N))
    matrix = [[0 for i in range(N)]for j in range(N)]
    numberList = list(range(1, N+1))

    ##### Main Program #####
    print("\n\nActual Solution \n")
    fill_grid(matrix)
    print_matrix(matrix)

    print("\n\nPuzzle \n")
    remove_k_cells(matrix, 20)
    print_matrix(matrix)

if __name__ == "__main__":
    main()