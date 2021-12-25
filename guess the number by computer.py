from random import randint
min = 1
max = 99
guess = 0
user = '0'
while user != 'd':
    guess = randint(min, max)
    print('your guess is %i' %guess)
    user = str(input('k or b or d: '))
    if user == 'b':
        print('my number is larger.')
        min = guess
        guess = randint(min, max)
        print('the minimum is %i' % min)
        print('the maximum is %i' % max)
    if user == 'k':
        print ('my number is smaller.')
        max = guess
        guess = randint(min, max)
        print('the minimum is %i' % min)
        print('the maximum is %i' % max)
    if user == 'd':
        print('***your guess was %i and it was correct***' % guess)
        break
        


