# types of puzzles

# ez 01 02 06 10

# med 03 04 07 11 14

# hard 05 08 09 12 15 16

# Function parses a file and return the question

def parseSudokuFile(filename):

    with open(filename) as f:

        question = []

        for i in range(9):
            num = f.readline().split()
            dummy = []
            for j in range(len(num)):
                dummy.append(int(num[j]))

            question.append(dummy)

    return (question)

# Function print out the puzzle

def print_puzzle(p):

    for d in range(9):

        for c in range(9):

            if c == 8:

                print(str(p[d][c]))

            else:

                print(str(p[d][c]) + " ", end="")


# find next cell to fill

# X checks for cells in x axis

# Y checks for cells in y axis

# P = puzzle

def findNextCell(p):

    for x in range(len(p)):

        for y in range(len(p[x])):

            if p[x][y] == 0:

                return x, y

    return -1, -1



'''# p = puzzle

# i = rows

# J = columns

# a = an entry in the cell

# // floor division

def entryisValid(p, i, j, a):

    rowvalid = all([a != p[i][x] for x in range(9)])

    if rowvalid:

        columnvalid = all([a != [x][j] for x in range(9)])

        if columnvalid:

            TopR = i -i % 3

            TopL = j - j % 3

         for i in range():



    ##check diagongals next



# checks horizontal & vertical 1 x's and x's 1

# check x -1 , y -1 '''

# r = rows

# c = columns

# a = an entry in the cell

# // floor division

def entryIsValid (p, r, c, a):
    
    # check a value in column c for row 1 to row 9:
    for x in range(9):

        if p[x][c] == a and x != r:
            return False
    
    # check a value in row y for column 1 to column 9:
    for y in range(9):

        if p[r][y] == a and y != c:
            return False    
    
    # check a value in small square:
    # rows in small square = row of big puzzle//3
    # column in small square = column of big puzzel//3
    # each small square has smallrow, small column
    smallrow = r//3
    smallcolumn = c//3

    for x in range (smallrow*3, smallrow*3+3):
        for y in range (smallcolumn*3, smallcolumn*3+3):
            if p[x][y] == a and x != r and y != c:
                return False
    return True


def solvePuzzle(p):
    ''' - find blank cell
        - for each value from 1 to 9: 
            + check value (from 1 to 9) is valid  for the blank cell (check column, then check row, then check small square that the blank cell is in)
            + after check: 
                + If the value is satisfued for blank cell, put the value to blank cell
                + If not, the value of blank cell = 0
            + If the value of blank cell is 0 after checking, keep continue to run the loop with next value '''

    # set variable for the return of findNextCell function
    blank1, blank2 = findNextCell(p)
    if blank1 == -1: # if blankcell is not = 0
        return True, p
    else:
        r, c = blank1, blank2    # row and column of blankcell
    
    #check value from 1 to 9 for each blankcell
    for i in range (1,10):
        if entryIsValid(p, r, c, i):
            p[r][c] = i     # if blank cell is satisfied when check the value i in it, the blankcell will have value i
            boo, check = solvePuzzle(p)
            if boo:
                return True, p # the blank cell is solved
            
            else:
                p[r][c] = 0 # the blank cell value will be 0, and keep continuing the loop until find the value i for blank cell
    return False, p    


def main():

    y = 'y'

    while y.lower() == 'y':

        # User enter the filename.txt

        question = parseSudokuFile(input("Please enter the file name: "))

        # Parse the file and print out the problem

        print_puzzle(question)

        # Solve the puzzle

        boo, answer = solvePuzzle(question)
        print()

        # Print out the answer
        print_puzzle(answer)
        print()
        y = input("Would you like to solve another Sudoku? [y/n]")
        print()


if __name__ == "__main__":

    main()

    """ 1 touple for sudoku 

    Need: 1 touple for a attributes for values in the first sudoku 

    Part of that touple we need values it can be assigned and its constraints (unassined values it connects to)

    Second sudoku that can change and update for backtracking purposes

    Def: checker - checks values against itself (if 9 checks how many it changes in next cells )

     Changer - 

     create new tree > see waht can change > change in new tree > print updated new tree 

     Check if tree is finished> return sudoku > check sudoku again and see what cna be changed 

     

     Erick: implement checker - what value do you want ot check? checks values that have already been assigned 

     ex: 4 is checked, every 0 in second touple (second touple) , should have 2 values for each cell (assinged & unassigned) - for default array

     """
