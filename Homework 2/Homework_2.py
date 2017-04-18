#HOMEWORK 2 - ALVIN V. HUYNH - 1477121
import random

#starting values
killIndic = 'Y'
weap = 4
botWeap = None
loop = 3
gameCounter = 1
aiCounter = 0
userCounter = 0

#reset values
def resetValues():
    global weap
    global loop
    global gameCounter
    global aiCounter
    global userCounter
    weap = 4
    loop = 3
    gameCounter = 1
    aiCounter = 0
    userCounter = 0

#introduction and welcome messages
def introMessage():
    global loop
    loop = 3
    print('\nHOMEWORK 2 - ALVIN V. HUYNH - 1477121')
    print('\nWecome to ROCK, PAPER, SCISSORS!')
    print('Here you will battle against an AI - to the death - for the best two out of three matches: RPS TOURNAMENT!')
    print('\nROCK destroys SCISSORS. PAPER destroys ROCK. SCISSORS destroys PAPER.')
    print('\nThe game starts NOW! Good luck!\n')

#user input for weapon
def userInput():
    print('| R - Rock | P - Paper | S - Scissors |')
    weap = str(input('Choose your weapon of choice: '))
    if(weap not in ('R', 'P', 'S', 'r', 'p', 's')):
        print('Invalid input.\n')
        return 4
    else:   #R = 1, P = 2, S = 3
        if(weap in ('R', 'r')):
            weap = 'rock'
        elif(weap in ('P', 'p')):
            weap = 'paper'
        else:
            weap = 'scissors'
        return weap

#ai weap assigned
def assignBotWeap():
    global botWeap
    botRando = random.randint(1,100)
    if(botRando < 33):
        botWeap = 'rock'
    elif(botRando < 66):
        botWeap = 'paper'
    else:
        botWeap = 'scissors'
    return botWeap


#simulates match and determines result
def simulate(weap, botWeap):
    global loop
    global gameCounter
    global userCounter
    global aiCounter
    
    gameCounter = gameCounter + 1
    
    #matches weapons
    if(weap == botWeap):
        result = 'D'
    elif(weap == 'rock' and botWeap == 'scissors'):
        result = 'W'
    elif(weap == 'paper' and botWeap == 'rock'):
        result = 'W'
    elif(weap == 'scissors' and botWeap == 'paper'):
        result = 'W'
    else:
        result = 'L'
    #determines results
    if(result == 'W'):
        userCounter = userCounter + 1
        loop = loop - 1
        print('\nRound ++ WON ++\nUser Score: ' + str(userCounter) + ' | AI Score: ' + str(aiCounter))
    elif(result == 'L'):
        aiCounter = aiCounter + 1
        loop = loop - 1
        print('\nRound -- LOST -- \nUser Score: ' + str(userCounter) + ' | AI Score: ' + str(aiCounter))
    else:
        print('\n== DRAW == \nUser Score: ' + str(userCounter) + ' | AI Score: ' + str(aiCounter))
        return 1

#determines result of the tournament
def determineFinal(userCounter, aiCounter):
    global killIndic
    global gameCounter
    killIndic = 'O'
    if(userCounter > aiCounter):
        print('\n========== +++ TOURNAMENT WON! +++ ==========')
    else:
        print('\n========== --- TOURNAMENT LOST! --- ==========')
    print('User Score: ' + str(userCounter) + ' | AI Score: ' + str(aiCounter))
    print('Rounds played: ' + str(gameCounter - 1))
    
#kill sequence
def killIndicator():
    global killIndic
    killIndic  = input('\nReplay? (Y/N): ')
    if(killIndic not in ('Y', 'y', 'N', 'n')):
        print('Invalid input.')
        killIndic = 'O'
    else:
        if(killIndic in ('Y', 'y')):
            killIndic = 'Y'
        else:
            killIndic = 'N'

#main sequence
while(killIndic in ('Y', 'y')):
    resetValues()
    introMessage()
    while(loop != 0):
        print('===== GAME ' + str(gameCounter) + ' =====')
        while(weap == 4):
            weap = userInput()
        botWeap = assignBotWeap()
        result = simulate(weap, botWeap)
        print('You played ' + weap + '. AI played ' + botWeap + '.\n')
        weap = 4
    determineFinal(userCounter, aiCounter)
    while(killIndic == 'O'):
        killIndicator()
    
    
