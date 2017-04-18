#HOMEWORK 3: PART 2 - ALVIN V. HUYNH - 1477121

killIndic = False
validInput = ('y', 'yes', 'n', 'no')

#intro message
print('\nALVIN HUYNH - HOMEWORK 3: PART 2 - 1477121\n')
print("This program is made to count the amount of letters in each of the user's word of the input.", end =' ')
print("The program will only read up to ending puncutation marks.\nType /help to see accepted characters.")

while killIndic == False:
    #starting varibales
    engAlphaList = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    engCharList = (' ', ',', ':', ';', '"', "'")
    letterCount = []
    userListProcess = []
    userListRaw = []
    userIndexValue = 0
    userInput = '/help'
    userInputBuild = ''

    while userInput == '/help':
        userInput = input('\nSentence: ')
        userListProcess[:0] = userInput.lower()
        if userInput == '/help':
            print('Acceptable characters: ')
            print(engAlphaList); print(engCharList)

    #processes user input to display raw format
    for userIndexValue in userListProcess:
        if userIndexValue in engAlphaList:
            userInputBuild = userInputBuild + userIndexValue
        elif userIndexValue in engCharList:
            if userInputBuild != '':
                userListRaw.append(userInputBuild)
            userInputBuild = ''
    if userInputBuild != '':
        userListRaw.append(userInputBuild)

    print(userListRaw) #prints user's raw words

    #counts amount of letters of user's words
    for userIndexValue in userListRaw:
        letterCount.append(len(userIndexValue))

    print(letterCount) #prints nubmer of letters in user raw words

    #kills or continues program
    killIndic = str.lower(input('\nKill program? (Y/N): '))
    while killIndic not in validInput:
        killIndic = input('Invalid input.\n\nKill program? (Y/N): ')
    if killIndic in (validInput[2], validInput[3]):
        killIndic = False


