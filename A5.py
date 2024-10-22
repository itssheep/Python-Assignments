# using the grid module from A5, we now make the robot move through the room.

import grid

def checkPath(path, start_pos = [0,0]):
    """
    This function checks whether a given path is a feasible path for the robot.
    The function returns a tuple containing the feasibility, last feasible position
    of the robot, and the number of valid steps the robot took.
    inputs
        path	: A 1D list containing the dirctions of the step ('N', 'E', 'S', 'W').
                 The list can be of any length.
        start_pos: A list containing the row number and the column number of the starting
                   position of the robot.
    Outputs:
        A tuple containing three elements,
        1. A string showing the feasibility
        2. A list containing the row and column number of the last feasible position of the path
        3. An integer returning the number of valid steps the robot took.
        """
    
    steps = 0
    feas = 'unknown'
    for d in path:
        
        ch = grid.checkNextStep(start_pos, d, grid=grid.grid, width=grid.width)
        if ch == 'invalid' or ch == 'obstacle':
           feas = 'obstacle'
           direc = start_pos
           break
        elif ch == 'out of bound':
            feas = 'out of bound'
            direc = start_pos
            break

        else:
            feas = 'feasible'  
            steps += 1
            direc = start_pos
            if d == 'N':
                start_pos[0] -= 1
            elif d == 'S':
                start_pos[0] += 1
            elif d == 'E':
                start_pos[1] += 1
            elif d == 'W': 
                start_pos[1] -= 1
            else:
                return 'invalid'

            if ch == 'Hooray':
                feas = 'goal'
                break

    return (feas, direc, steps)

def navigateGrid(start_pos = [0,0]):
  """
    This function takes the user inputs and move the robot around the grid. The function
    should request user input until the user decides to quit the navigation.
    
    inputs:
        start_pos: A list containing the row number and the column number of the starting
                   position of the robot.
    outputs:
        A tuple containing three elements,
        1. A string showing the completion or the goal reached
        2. A list containing the row and column number of the current position of the robot
        3. An integer returning the number of valid steps the robot took since the start of this function.
    """
    dire = start_pos
    steps = 0
    while True:
        validdir = ['N','E','S','W','Q']

        i = input('N, E, S, W, Q? ')
        if i not in validdir:
            return 'invalid'
        elif i != 'Q':
            p = grid.checkNextStep(start_pos, i, grid=grid.grid, width=grid.width)
        if i == 'N':
            if p == 'obstacle':
                print('obstacle')
            elif p == 'out of bound':
                print('out of bound')
            elif p == 'Hooray':
                return ('goal',dire,steps)
            else:
                dire[0] -= 1
                steps += 1
                if p == 'Hooray':
                    return ('goal',dire,steps)

        elif i == 'S':
            if p == 'obstacle':
                print('obstacle')
            elif p == 'out of bound':
                print('out of bound')
            else:
                dire[0] += 1
                steps += 1
                if p == 'Hooray':
                    return ('goal',dire,steps)

        elif i == 'E':
            if p == 'obstacle':
                print('obstacle')
            elif p == 'out of bound':
                print('out of bound')
            else:
                dire[1] += 1
                steps += 1
                if p == 'Hooray':
                    return ('goal',dire,steps)

        elif i == 'W':
            if p == 'obstacle':
                print('obstacle')
            elif p == 'out of bound':
                print('out of bound')
            else:
                dire[1] -= 1
                steps += 1
                if p == 'Hooray':
                    return ('goal',dire,steps)

        elif i == 'Q':
            return ('done', dire, steps)
        else:
            return 'invalid'
        

    

if __name__ == '__main__':
    
    #Test your code here
    
    print(checkPath(['E','E','S','W','S','W'], [0,0]))
    print(checkPath(['E', 'S', 'E', 'E', 'E', 'E', 'E','N'], [3,1]))

    print(navigateGrid())
