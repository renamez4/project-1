#This program demostrates two functions that
#have local variables with the same name.

def main():
# Call the texas function.
    texas()
# Call the california function.
    california()
# Definition of the texas function. it creates
# a local ariable named birds.
def texas():
    birds = 50000
    print('texas has', birds, 'birds.')
# Definition of the cali fornia funtion. It also
# creates a local variable named birds.
def california():
    birds = 8000
    print('califonia has' , birds, 'birds.')

# call the main function.
main()