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



@task
def task_2_2():
    pass
    move_down()
    for i in range(4):
        fill_kreuz()
        vpravo()
    fill_kreuz()
    move_left(n=2)
    move_up()
    


if __name__ == '__main__':
    run_tasks()
