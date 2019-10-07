#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    pass
    while not wall_is_on_the_right() and (wall_is_above() and wall_is_beneath()):
        move_right()
    if not wall_is_above():
        move_up()
    elif not wall_is_beneath():
        move_down()
    else:
        while not wall_is_on_the_left() and (wall_is_above() and wall_is_beneath()):
            move_left()
        if not wall_is_above():
            move_up()
        elif not wall_is_beneath():
            move_down()
            k+=1
    while not wall_is_on_the_left():
        move_left()
    while not wall_is_above():
        move_up()


if __name__ == '__main__':
    run_tasks()
