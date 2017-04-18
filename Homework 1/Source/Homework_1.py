#Alvin Huynh - 1477121
#Homework 1 - Assigned Thursday, Septemder 08, 2016
#Due on Thursday, September 15, 2016

def challengeTwo():
    #CHALLENGE 2
    print('\nCHALLENGE 2\n')
    print('Only works for integers between 0 and 31.\n')
    number = int(input('Number used for bianry conversion: '))
    
    if(number >= 0 and number <= 31):
        print('{0:b}'.format(number))
    else:
       print('User input value not in range.')
       challengeTwo()

skipChallenge = int(input('\nSkip challenge 1 (1/0)?: '))

if(skipChallenge == 0):
    
    #CHALLENGE 1
    print('\nCHALLENGE 1\n')
    
    
    tax = .08
    
    fries = 5.00
    steak = 16.00
    pasta = 12.00
    vege = 12.00
    iceCream = 6.00

    print('Welcome to THE RESTAURANT!\nPlease type 1/0 if you want or do not want the following dishes.\n')

    fries1 = int(input('Fresh Potato Fries ($5.00): '))

    steak1 = int(input('Garlic Butter Steak ($16.00): '))
    pasta1 = int(input('White Wine Sauce w/ Linguine ($12.00): '))
    vege1 = int(input('Ratatouille w/ Olive Oil Sauce ($12.00): '))

    iceCream1 = int(input('Ice Cream Flavor of Choice w/ Syrup ($6.00): '))

    subtotalPrice = (fries * float(fries1)) + (steak * float(steak1)) + (pasta * float(pasta1)) + (vege * float(vege1)) + (iceCream * float(iceCream1))
    taxes = subtotalPrice * tax
    totalPrice = taxes + subtotalPrice

    print('\nSubtotal: $' + format(subtotalPrice, '.2f'))
    print('Taxes (8%): $' + format(taxes, '.2f'))
    print('Total: $' + format(totalPrice, '.2f'))

    print('\nThank you for choosing THE RESTAURANT! Your order will be sent out as soon as possible!')

    x = 1
    challengeTwo()

else:
    challengeTwo()
