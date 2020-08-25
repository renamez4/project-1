def main():
    first_name, last_name = get_name()
    print('first name: ',first_name,'Last name :',last_name)
    password(first_name,last_name)
    
def get_name():
    #Get ther user's first and last names.
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    #Return both names.
    return first,last

def password(f,l):
    if len(l) % 2 == 0 :
        print("My password: ",f[:3]+(l)[(len(l)//2)-2:(len(l)//2)+1])
    else:
        print("My password: ",f[:3]+(l)[(len(l)//2)-1:(len(l)//2)+2])

main()