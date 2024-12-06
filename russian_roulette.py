from random import *
input('Welcome To russian Roulette By Simearduino (Press Enter To Continue)')
def russianRoulette(x):
    input('Press Enter To Start')
    while True:
        r=randint(1,x)
        if r!=1:
            for i in range(15):
                print()
            print('Next Player'+str(x-1)+' Max Attemps Left')
            print()
            input('Press Enter To Shoot')
            x=x-1
        else:
            for i in range(15):
                print()
            print('Bang')
            break
russianRoulette(int(input('Nb Of Max Attemps : ')))