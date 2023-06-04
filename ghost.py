# mogs ghost game
from random import randint

print('Ghost Game ')
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint (1, 4)
    print('Three doors ahead...')
    print('A ghost behind one .')
    print('which door do you open?')
    door = input('1,2, 3 or 4?')
    try:
        door_num = int(door)
        if door_num == ghost_door:
            print('GHOST!')
            feeling_brave = False
        elif door_num > 4:
            print('Dont cheat - number less than 4 please - deduct a point !!')
            score = score -1 
        else:
            print ('No ghost!')
            print('You enter the next room.')
            score = score + 1
    except ValueError:
        print('Thats not a number !!')
print('Run away!')
print('Game over! You scored ', score)
















