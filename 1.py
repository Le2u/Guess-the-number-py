from random import randint

x = randint(0 , 100 )
for count in range (0 , 7):
    print 'Please input a number between 0 ~ 100.You have only seven chances.'
    digit = input()
    if digit == x :
        print 'Bingo!'
    elif digit > x :
        print 'Too large,please try again.'
    else :
        print 'Too small,please try again.'
