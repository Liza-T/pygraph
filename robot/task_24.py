#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
    pass
    move_right()
    move_down(n=2)
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
    move_left(n=2)
    move_up()
    


if __name__ == '__main__':
    run_tasks()
