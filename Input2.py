1 # Get the user's name, age, and income.
name = input('what is your name')
age = int (input('what is your age ?'))
income = float(input('what is your income?'))
# Display the data.
print('Here is the data you entered:')
print('Name:',name)
print('age:',age)
print('income:',format(income,'12,.2f'))