import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]


def possible(y,x,n):
        global grid
        for i in range(0,9): #checks if number is already present in row
                if grid[y][i] == n:
                        return False
        for i in range(0,9): #checks if number is already present in Column
                if grid[i][x] == n:
                        return False
        x0 = (x//3)*3
        y0 = (y//3)*3
        for i in range(0,3): #checks if number is already present in 3x3 section
                for j in range(0,3):
                        if grid[y0+i][x0+i] == n:
                                return False
        return True

def solve():
        global grid
        for y in range(9):
                for x in range(9):
                        if grid[y][x] == 0: #loops until finds "blank" space AKA 0
                                for n in range(1,10):
                                        if possible(y,x,n):
                                                grid[y][x] = n #inputs current number is possible entry
                                                if solve(): #runs solve recursivly
                                                        return True #once puzzle is solved correctly, returns true
                                                grid[y][x] = 0 #if a cell has no possible numbers, undoes all previous entries until arrives at a cell with another untested possible number
                                return False #if all possibilities have been attempted and no solution was found, returns false
        return True
        
def first_check():
        global grid
        count = 0
        for y in range(9):
                for x in range(9):
                        n = grid[y][x]
                        if n != 0:
                                grid[y][x] = 0
                                if possible(y,x,n) == False:
                                        count = count + 1
                                grid[y][x] = n
        if count > 1:
                return False
        else:
                return True




print("Your initial Sudoku puzzle:\n")
print(np.matrix(grid))
if first_check():
        if solve():
                print("The solution to the sudoku puzzle:")
                print(np.matrix(grid))
        else:
                print("No solution found: this is not a solvable sudoku puzzle.")
else:
        print("The provided puzzle does not follow the constraints.")