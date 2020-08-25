#this program simulatte 10 tosses of a coin.
import random#constants
Heads = 1 
Tails = 2
Tosses = 20
Head = 0
Tail = 0
def main():
    global Head
    global Tail
    for toss in range(Tosses):
        #simulate the coin toss.
        if random.randint(Heads,Tails) == Heads:
            print('Heads')
            Head = Head + 1 
        else:
            print('Tails')
            Tail = Tail + 1
    print('Head',Head)
    print('Tail',Tail)
    print('Tosses',Tosses)        
#call the main function.
main()
