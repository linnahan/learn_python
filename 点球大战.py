from random import choice
score=[0,0]
direction = ['left', 'center', 'right']
def run():
    print('==== You Kick! ====')
    print('Choose one side to shoot:')
    print('left, center, right')
    you =input()
    print('You kicked ' + you)
    com = choice(direction)
    print('Computer saved ' + com)
    if you != com:
        print('Goal!')
        score[0]+= 1
    else:
        print('Oops...')
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))
    print('==== You Save! ====')
    print('Choose one side to save:')
    print('left, center, right')
    you =input()
    print('You saved ' + you)
    com = choice(direction)
    print('Computer kicked ' + com)
    if you == com:
        print('Saved!')
    else:
        print('Oops...')
        score[1]+= 1
    print('Score: %d(you) - %d(com)\n' % (score[0], score[1]))
for i in range(5):
    print('==== Round%d ===='%(i+1))
    run()
while score[0]==score[1]:
    i+=1
    print('==== Round%d ===='%(i+1))
    run()
if score[0]>score[1]:
    print('You win!')
else:
    print('You lose')