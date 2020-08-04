score1 = int(input('Enter the score for test 1:'))
score2 = int(input('Enter the score for test 2:'))
score3 = int(input('Enter the score for test 3:'))
score_all = ( score1 + score2 + score3 ) / 3
print("\n Average",score_all)
if score_all > 95 :
    print("Congratulation!\n Congrat Guy Lucky")