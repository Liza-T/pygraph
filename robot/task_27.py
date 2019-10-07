#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    pass
    b = True
    m=1
    move_right()
    fill_cell()
    while b:
        k=0
        for i in range(m):
            if not wall_is_on_the_right():
                move_right()
                k+=1
            else:
                b = False
        if b or k==m:
            fill_cell() 
        m+=1
            
        

if __name__ == '__main__':
    run_tasks()
