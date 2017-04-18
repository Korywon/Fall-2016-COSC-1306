#HOMEWORK 3 - PROBLEM 1 - ALVIN V. HUYNH - 1477121

print('\nHOMEWORK THREE (3) - PROBLEM 1 (1) - 1477121')
print("\nThis program is designed to detect if the user's input contains all the letters of the alphabet. It does not detect for correct English syntax, grammar, and spelling for the sake of simplicity.")
print('\nIt is able to account for duplicate ocurrences of a letter.')

killIndic = False
validInput = ('y', 'yes', 'n', 'no')

while killIndic == False:
    #starting variables
    alphaCount = 0
    alphaIndex = 0
    counter = 0
    userIndex = 0
    userIndexValue = 0
    alphaList1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    alphaList2 = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 0],
                 ['o', 0], ['p', 0], ['q', 0], ['r', 0], ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]
    userList = []
    testResult = True

    #calls and refines user input
    userList[:0] = str.lower(input('\nSentence: '))
    userList.sort()

    #finds where alphabetical characters start in user input
    for userIndexValue in userList:
        if userIndexValue not in alphaList1:
            userIndex = userIndex + 1
        else:
            break

    #compares validity (main sequence)
    for alphaIndex in alphaList1:
        for userIndexValue in userList[userIndex:]:
            if userIndexValue == alphaIndex:
                alphaList2[alphaCount][1] = alphaList2[alphaCount][1] + 1
                counter = counter + 1
            else:
                break
        if(alphaList2[alphaCount][1] == 0):
            testResult = False
            break
        elif(alphaIndex == 'z'):
            break
        alphaCount = alphaCount + 1
        userIndex = userIndex + counter
        counter = 0

    #prints output
    print(testResult)

    #kills or continues program
    killIndic = str.lower(input('\nKill program? (Y/N): '))
    while killIndic not in validInput:
        killIndic = input('Invalid input.\n\nKill program? (Y/N): ')
    if killIndic in (validInput[2], validInput[3]):
        killIndic = False

