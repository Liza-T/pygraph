#!/usr/bin/python3

from pyrob.api import *

def vyhod():
    while not wall_is_above():
        move_up()
    while not wall_is_on_the_left():
        move_left()
@task
def task_8_29():
    pass
    while not wall_is_on_the_left() and wall_is_above():
        move_left()
    if not wall_is_above():
        vyhod()
    else:
        while not wall_is_on_the_right() and wall_is_above():
            move_right()
        if not wall_is_above():
            vyhod()


if __name__ == '__main__':
    run_tasks()
