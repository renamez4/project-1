score = int(input('Enter a test score: '))
while score <0 or score > 100:
    print(' Error : the score cannot be negative')
    print(' or gteater than 100.')
    score = int(input('Enter the correct score: '))