#This program demonstrates passing two string
#arguments to a function.
def reverse_name(first, last):
    print(last[::-1],first[::-1])
def main():
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    print('Your name reversed is ')
    reverse_name(first_name, last_name)
    
#call the main function.
main()
