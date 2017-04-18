#CHALLENGE 2 - Alvin V. Huynh - PSID 1477121 - Tuesday, September 13, 2016

print('\nCHALLENGE TWO - ALVIN V. HUYHH - 1477121\n')

killIndicator = 'Y'

#user input
def promptInput():
    print('\nNote, this program only converts up to 5 bits. (0 - 31)')
    number = int(input('Decimal number to binary: '))
    return number

#kill indicator
def promptKill():
    killValue = str(input('\nRestart? (Y/N): ')) #kill indicator
    return killValue

#conversion
def decimalToBinary(number): 
    if(number >= 0 and number <= 31):
        binary = str('{0:b}'.format(number)) #conversion
        counter = len(binary) #character counter     
        if(counter != 5):
            print('\nBinary: ' + ((5 - counter) * '0') + binary) #adds leading zeroes
        else:
            print('\nBinary: ' + binary)
    else:
        print('ERROR_2: User input not in range (0 - 31).') #error return

#main sequence
while(killIndicator in ('Y', 'y')):
    number = promptInput() #prompt user input
    decimalToBinary(number) #function call using input
    killIndicator = promptKill() #repeat or kill program
    if(killIndicator not in ('Y', 'y', 'N', 'n')):
        while(killIndicator not in ('Y', 'y', 'N', 'n')): #detects invalid inputs
            print('ERROR_3: Invalid input.')
            killIndicator = promptKill()
    if(killIndicator in ('N', 'n')):
        print('\nPROGRAM ENDING.')
