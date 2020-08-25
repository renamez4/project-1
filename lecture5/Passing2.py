#this program demonstrates a function that accepts
#two arguments.
def main():
    num1 = int(input('Blank: '))
    num2 = int(input('Blank: '))
    print('The sum of is')
    show_sum (num1,num2)
#The show_sum function accepts two argu,ents
#and displays their sum.
def show_sum(num1, num2):
    result = num1 + num2
    print(result)
#call the main function.
main()