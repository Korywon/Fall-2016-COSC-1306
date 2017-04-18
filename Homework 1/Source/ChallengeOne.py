#CHALLENGE 1 - Alvin V. Huynh - PSID 1477121 - Tuesday, September 13, 2016
print('\nCHALLENGE 1 - ALVIN V. HUYNH - 1477121\n')

#fixed variables
tax = .08
fries = 5.00
steak = 16.00
pasta = 12.00
vege = 12.00
iceCream = 6.00

#welcome message
print('Welcome to THE RESTAURANT!\nPlease type 1/0 if you want or do not want the following dishes.\n')

#user input
fries1 = int(input('APPETIZERS\nFresh Potato Fries ($5.00): '))
steak1 = int(input('\nENTREES\nGarlic Butter Steak ($16.00): '))
pasta1 = int(input('White Wine Sauce w/ Linguine ($12.00): '))
vege1 = int(input('Ratatouille w/ Olive Oil Sauce ($12.00): '))
iceCream1 = int(input('\nDESSERT\nIce Cream Flavor of Choice w/ Syrup ($6.00): '))

#calculations
subtotalPrice = (fries * float(fries1)) + (steak * float(steak1)) + (pasta * float(pasta1)) + (vege * float(vege1)) + (iceCream * float(iceCream1))
taxes = subtotalPrice * tax
totalPrice = taxes + subtotalPrice

#print message
print('\nSubtotal: $' + format(subtotalPrice, '.2f'))
print('Taxes (8%): $' + format(taxes, '.2f'))
print('Total: $' + format(totalPrice, '.2f'))

print('\nThank you for choosing THE RESTAURANT! Your order will be sent out as soon as possible!')

input('\nPress the ENTER key to end...')
