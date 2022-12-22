# import math for pow 
import math

# print choice message
# using ---- as divides to give a better appearance
print('Choose either:     \'investment\'     or      \'bond\'')
print('------------------------------------------------------------------------------------')
print('investment   -   to calculate the amount of interest you\'ll earn on your investment')
print('bond         -   to calculate the amount you\'ll have to pay on a home loan')
print('------------------------------------------------------------------------------------')

# get user input which calc they want to use
choice = input('Enter choice: ')
print('----------------------------------------------------------')

# if statement for investment or bond
# if investment
if choice.lower() == 'investment':
    # get user input amount cast to float
    amount = float(input('Enter amount:                          £'))
    print('----------------------------------------------------------')
    # get user input interest rate cast to int
    rate = int(input('Enter interest rate:                   %')) / 100
    print('----------------------------------------------------------')
    # get user input years to invest cast to int
    time = int(input('Enter years to invest:                  '))
    print('----------------------------------------------------------')
    # get user input interest type
    interest = input('Enter \'simple\' or \'compound\':          ')
    print('----------------------------------------------------------')

    # if statement for interest type
    # if simple
    # using .lower to validate more inputs
    if interest.lower() == 'simple':
        # calc total using round to 2
        total = round(amount * (1 + rate * time),2)
        # print total return with f string
        print('                   Total return')
        print(f'                    £{total}')
        print('----------------------------------------------------------')
    # else if compound
    # using .lower to validate more inputs
    elif interest.lower() == 'compound':
        # calc total using math import and round to 2
        total = round(amount * math.pow((1 + rate), time), 2)
        # print results including f string
        print('                  Total Return:')
        print(f'                    £{total}')
        print('----------------------------------------------------------')
    # else input not reconiged 
    else:
        # print error message
        print('''
              !ERROR!
        Input not recogised. 

         Please only enter:

              \'simple\'

                 or
            
             \'compound\'
              ''')
        print('---------------------------------------------------------')

# else if bond
# using .lower to validate more inputs
elif choice.lower() == 'bond':
    # get user input cost cast to float
    cost = float(input('Enter the house cost:              £'))
    print('----------------------------------------------------------')
    # get user input rate cast to int
    rate = (int(input('Enter interest rate:               %')) / 100) / 12
    print('----------------------------------------------------------')
    # get user input month to repay
    time = int(input('Enter number of months to repay:    '))
    print('----------------------------------------------------------')
    # calc repay amount using round to 2
    repay = round((rate * cost) / (1 - (1 + rate) ** (-time)), 2)
    # print out result including f string
    print('               Monthly Repayments:')
    print(f'                    £{repay}')
    print('----------------------------------------------------------')
# else input not recognised 
else:
    #print error message
    print('''
              !ERROR!
        Input not recogised. 

         Please only enter:

            \'investment\'

                 or
            
               \'bond\'
              ''')
    print('---------------------------------------------------------')