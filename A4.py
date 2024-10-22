# In this assignment we create a room for a robot to walk around in, and make a function that checks if it can move to that position.

def getGridInd(row_no, column_no, grid, width):
    
 #   This function returns the index of the element in the list corresponding
 #   to the grid location represented by the row_no and column_no.
 #   inputs:
 #   row_no		: The row number (numbers starts from 0). [integer]
 #   column_no	: The column number (numbers starts from 0). [integer]
 #   grid 		: The list containing the information about the grid [integer]
 #   width 		: Width of the grid. This can be used to calculate the number of rows. [integer]
    
 #   returns: This function returns the index [integer]
    
 #   For more details check the Assignment 5 document.
    
    
    # Write your code here
    t = False

    Ind = str(row_no) + str(column_no)
  
    for i in Ind:
        if i.isnumeric() == False:
            Ind = -1
            t = True
            break
            
    if t == False:
        
        if column_no < 0:
            Ind = -1
        elif column_no > width:
            Ind = -1
        else:
            
            if int(Ind) > len(grid):
                Ind = -1
            elif int(Ind) < 0:
                Ind = -1
    
    Ind = int(Ind)
    return Ind

def checkNextStep(curr_pos, dir, grid, width):
    
  #  This function checks whether the robot can take the next step in the direction given by
  #  dir argument.
    
  #  inputs:
  #  curr_pos	: This contains the position of the robot. First element of the list gives
                the row number and the second element give the column number. [list]
  #  dir 		: Direction of the next move 'N' for north, 'E' for East, 'S' for South, and 'W' for west.
  #  grid 		: The list containing the information about the grid [integer]
  #  width 		: Width of the grid. This can be used to calculate the number of rows. [integer]
    
  #  returns: A string
  #  'invalid'	: Current position is outside of the grid or on an obstacle.
  #  'go' 		: Next position is free.
  #  'obstacle'	: Next position has an obstacle
  #  'out of bound': Next position is out of bound.
  #  'Hooray' 	: Next position is goal
  #  For more details check Assignment 5 document.
    
    # Write your code here
   
    rowPos = curr_pos[0]
    colPos = curr_pos[1]
    
    
    
    Ind = getGridInd(rowPos,colPos,grid,width)
    

    if Ind == -1 or str(rowPos).isnumeric() == False or str(colPos).isnumeric == False:
        return 'invalid'

    curr_pos = str(rowPos) + str(colPos)
    curr_pos = int(curr_pos)
    
    if len(grid) <= curr_pos:
        return 'invalid'
    
    if grid[curr_pos] == 'O':
        return 'invalid'


    maxRow = len(grid)//width
        
    validDir = ['N','E','S','W']
    
    
    if dir not in validDir:
        return 'invalid'
    else:
        if dir == 'N':
            rowPos -= 1
            
        elif dir == 'S':
            rowPos += 1

        elif dir == 'E':
            colPos += 1

        elif dir == 'W':
            colPos -= 1

        if colPos < 0 or rowPos < 0:
            return 'out of bound'

        curr_pos = str(rowPos) + str(colPos)
        curr_pos = int(curr_pos)

        if colPos < 0 or rowPos > maxRow or rowPos < 0 or curr_pos > len(grid):
            return 'out of bound'
        
        
        else:
            if grid[curr_pos] == 'F':
                return 'go'
            elif grid[curr_pos] == 'O':
                return 'obstacle'
            elif grid[curr_pos] == 'G':
                return 'Hooray'

if __name__ == '__main__':
    
   # This example refers to the grid given in the assignment.
   # However, your implementation should be able to handle a grid of any size
   # grid = ['F', 'F', 'F', 'F', 'F', 'F', 'O', 'F', 'F', 'F',\
   #         'F', 'F', 'O', 'F', 'F', 'O', 'F', 'O', 'F', 'F',\
   #         'F', 'O', 'O', 'F', 'F', 'F', 'F', 'F', 'O', 'F',\
   #         'F', 'F', 'F', 'O', 'O', 'O', 'O', 'F', 'O', 'F',\
   #         'F', 'O', 'F', 'F', 'F', 'F', 'G', 'F', 'F', 'F']
    
   # Width of this grid (Number of columns) is 10.
    


    # Write your test code here
    grid = ['F', 'F', 'F', 'F', 'F', 'F', 'O', 'F', 'F', 'F',\
            'F', 'F', 'O', 'F', 'F', 'O', 'F', 'O', 'F', 'F',\
            'F', 'O', 'O', 'F', 'F', 'F', 'F', 'F', 'O', 'F',\
            'F', 'F', 'F', 'O', 'O', 'O', 'O', 'F', 'O', 'F',\
            'F', 'O', 'F', 'F', 'F', 'F', 'G', 'F', 'F', 'F']
    width = 10
    
    print(checkNextStep([0,2],'W',grid,width))
