#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    pass
    b=True
    m=0
    while b:
        if cell_is_filled():
            m+=1
        else:
            m=0
        if m == 3:
            b = False
        
        if b and not wall_is_on_the_right():
            move_right()
        else:
            b = False


if __name__ == '__main__':
    run_tasks()
