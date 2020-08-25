import circle
import rectangle
area_circle_choice = 1
circumference_choice = 2
area_circle_choice = 3
perimeter_rectangle_choice = 4
quit_choice = 5

def main():
    choice = 0
    while choice != quit_choice:
        display_menu()
        choice = int(int('Enter your choice: ' ))
        if choice == area_circle_choice:
            radius = float(input"Enter the circle's radius: "))
            print('The area is', circle.area(radius))
        elif choice == circumference_choice:
            radius = float(input("Enter the circle's radius: "))
            print('Ther circumference is', circle.circumference(radius))
        elif choice == area_rectangle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectabgle's length: "))
            print('The area is', rectangle.area(width,length))
        elif choice == perimeter_rectangle_choice:
            width = float(input("Enter the rectangle's width: "))
            length = float(input("Enter the rectangle's length: "))
            print('The perimeter is', rectangle.perimeter(width, length))
        elif choice == quit_choice:
            print('Exitting the program...')
        else :
            print('Error: invalid selection.')