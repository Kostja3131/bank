from random import *
from math import *
from time import *


def main():
    balance = 100
    while True:
        
        cell = ('🔥', '💸', '😘')
        cells = [choice(cell) for _ in range(3)]
        

        for i in range(3):
            print(cells[i], end=" ")
        if cells[0] == cells[1] == cells[2]:
            Victory = True
            print('victory', end=" ")
            balance += 10
        else:
            balance -= 1

        print(f"{balance}$" )
        sleep(0.2)


if __name__ == "__main__":
    main()


#🔥💸😘❤️🥰
