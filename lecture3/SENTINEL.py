# this program calculates sales commissions.
# Create a variale to control the loop.
keep_going = 'y'
comm_rate = 2.5
# Calculate a series of commissions.
while keep_going == 'y' or keep_going == 'Y':
    # Get a salesperson's sales and commission rate.
    sales = float(input('Enter the amount of sale: '))
    

    # Calculate the commission.
    commission = sales * comm_rate

    # Display the commission.
    print('The commission is $', \
    format(commission, ',.2f'),sep= '')

    # See if the user wants to do another one.
    keep_going = input('Do you want to calculate another' + 'commission (Enter y for yes): ')
