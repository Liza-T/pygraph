#!/usr/bin/python3

from pyrob.api import *


def fill_kreuz():
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_up()
    fill_cell()
    move_down(n=2)
    fill_cell()
    move_up()
    move_right()
    fill_cell()

def vpravo():
    move_right(n=2)
    move_up()

def vniz():
    move_left(n=38)
    move_down(n=3)

@task(delay=0.02)
def task_2_4():
    pass
    for i in range(5):
        for j in range(10):
            fill_kreuz()
            if j != 9:
                vpravo()
        if i != 4:
            vniz()
    move_left(n=38)
    move_up()


if __name__ == '__main__':
    run_tasks()
