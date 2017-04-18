#Homework 4 - Alvin V. Huynh - 1477121

import random
East = ['c', 'f', 'g','w']
West = []
Forbidden = [['c','g','w'], ['c','g'], ['g','w']]


#Complete the following function so it Prints the objects at East and then the objects at West
def PrintContains(East,West):
    print('East: ')
    for x in East:
        print(x.upper(), end = ' ')
    print('\n\nWest: ')
    for x in West:
        print(x.upper(), end = ' ')
    print('\n')
    

#Go west: Complete this function according to the instructions on HW4
def GoWest(East, West):
    forbid = True
    
    while forbid == True: #finds solution
        entity = 'f'
        
        while entity == 'f': #chooses random non-farmer entity
            entity = random.choice(East)

        #moves entity to west side
        West.append(entity)
        East.remove(entity)

        #moves farmer to east side
        West.append('f')
        East.remove('f')

        for x in Forbidden: #checks validity of east side
            if x == East:
                forbid = True
                East.append(West[len(West) - 1])
                East.append(West[len(West) - 2])
                del West[len(West) - 1]
                del West[len(West) - 1]
                East.sort()
            else:
                forbid = False
            if forbid == True:
                break

    West.sort()
    PrintContains(East, West)
    print('-------------------------------------\n')
    return East, West
    

#Go East: Complete this function according to the instructions on HW4   
def GoEast(East,West):
    #moves farmer to east side
    East.append('f')
    West.remove('f')
    
    for x in Forbidden: #check validity of west side and moves random entity if necessary
        if x == West:
            move = random.choice(West)
            East.append(move)
            West.remove(move)
    
    PrintContains(East, West)
    print('-------------------------------------\n')
    return East, West
    

# Solution: This function returns True if all objects are on the West side otherwise returns False (One line of code)    
def Solution():
    if len(East) == 0:
        return True
    

#DO not change anything in the following lines. Your job is to complete the functions above.
PrintContains(East, West)
print('-------------------------------------')  
condition = True
while condition:
    East, West = GoWest(East, West)
    if not Solution():
        East, West = GoEast(East, West)
    else:
        condition = False
