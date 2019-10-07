#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    pass
    for i in range(12):
        for j in range(27):
            move_right()
            fill_cell()
        move_down()
        move_left(n=27)
    move_right()

if __name__ == '__main__':
    run_tasks()
