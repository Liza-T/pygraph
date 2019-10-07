#!/usr/bin/python3

from pyrob.api import *
    


@task(delay=0.01)
def task_9_3():
    pass
    size = 1
    while not wall_is_on_the_right():
        move_right()
        size+=1
    move_left(n=size-1)
    for i in range(0, size):
        for j in range(0, size):
            if j != i and j != size-1 - i:
                fill_cell()
            if j != size-1:
                move_right()
        move_left(n=size-1)
        if i != size-1:
            move_down()
            
            
    

if __name__ == '__main__':
    run_tasks()
