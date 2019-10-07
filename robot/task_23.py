#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    m=0
    k=0
    move_right()
    while not wall_is_on_the_right():
        if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
                m+=1
            fill_cell()
            move_down(n=m)
            m=0
        move_right()
        k+=1
    if not wall_is_above():
            while not wall_is_above():
                move_up()
                fill_cell()
                m+=1
            fill_cell()
            move_down(n=m)
            m=0
    move_left(n=k+1)
       


if __name__ == '__main__':
    run_tasks()
