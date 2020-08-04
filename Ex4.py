print('Please select operation')
print('1. Add')
print('2. Subtract')
print('3. Multiply')
print('4. divide')
op = int (input('select operations form 1,2,3,4 : '))
num1 = int (input('Enter first number: '))
num2 = int (input('Enter second number : '))
if op == 1:
    print(num1 ,'+', num2,'=',num1 + num2 )
elif op == 2:
    print(num1 ,'-', num2,'=',num1 - num2 )
elif op == 3:
    print(num1 ,'*', num2,'=',num1 * num2 )
elif op == 4:
    print(num1 ,'/', num2,'=',num1 / num2 )



