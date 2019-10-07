#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    pass
    m=0
    while not wall_is_beneath():
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            m+=1
        fill_cell()
        move_left(n=m)
        move_down()
        k=m
        m=0
    for i in range(k):
        fill_cell()
        move_right()
    fill_cell()
    move_left(n=k)

if __name__ == '__main__':
    run_tasks()
