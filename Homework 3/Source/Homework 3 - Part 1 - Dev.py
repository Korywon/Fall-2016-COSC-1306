#HOMEWORK 3 - PROBLEM 1 - ALVIN V. HUYNH - 1477121

#``~~11!!22@@33##44$$55%%66^^77&&88**99((00))--__==++[[{{]]}}\\||;;::''"",,<<..>>//??  aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz
#We promptly judged antique ivory buckles for the next prize.

killIndic = False
validInput = ('y', 'yes', 'n', 'no')

while killIndic == False:
    #starting variables
    userIndex = 0 #indicates position of the start of alphabetical characters in user input
    userIndexValue = 0 #storage value for for loop
    alphaIndex = 0 #storage value for for loop
    alphaCount = 0 #adjusts position
    counter = 0 #adjusts position
    userList = [] #used to store the user input
    alphaList1 = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    alphaList2 = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0], ['j', 0], ['k', 0], ['l', 0], ['m', 0], ['n', 0],
                 ['o', 0], ['p', 0], ['q', 0], ['r', 0], ['s', 0], ['t', 0], ['u', 0], ['v', 0], ['w', 0], ['x', 0], ['y', 0], ['z', 0]]
    testResult = True #stores result of test

    #calls and refines for user input
    userList[:0] = str.lower(input('\nSentence: ')) #calls for user input
    userList.sort() #sorts the user input alphabetically
    print(userList)

    #finds where alphabetical characters start in user input
    for userIndexValue in userList:
        if userIndexValue not in alphaList1:
            userIndex = userIndex + 1
        else:
            break

    ##diagnostic coding   
    ##print(userList[userIndex])
    ##print(userIndex)

    #compares validity (main sequence)
    for alphaIndex in alphaList1:
        ##print(alphaIndex + ' ALPHA')
        for userIndexValue in userList[userIndex:]:
            ##print(userIndexValue + ' USER')
            if userIndexValue == alphaIndex:
                alphaList2[alphaCount][1] = alphaList2[alphaCount][1] + 1
                ##print(alphaList2[alphaCount][1], end = ' '); print('continue')
                counter = counter + 1
                ##print(counter)
            else:
                ##print(alphaList2[alphaCount][1], end = ' '); print('break')
                break
        if(alphaList2[alphaCount][1] == 0):
            testResult = False
            break
        elif(alphaIndex == 'z'):
            #print('\n')
            break
        alphaCount = alphaCount + 1
        userIndex = userIndex + counter
        counter = 0
        ##print('\n')

    #prints output
    print('\n'); print(testResult)

    #kills or continues program
    killIndic = str.lower(input('\nKill program? (Y/N): '))
    while killIndic not in validInput:
        killIndic = input('Invalid input.\n\nKill program? (Y/N): ')
    if killIndic in (validInput[2], validInput[3]):
        killIndic = False

