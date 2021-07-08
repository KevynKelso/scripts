#!/usr/bin/env python3
import sys
import click

PLANNER_LOCATION = "/Users/kkelso/Desktop/planner.txt"

# what defines an urgent task?
# - deadline is approaching

# File structure
# <name>, <priority>, <due>, <time to complete>



def display_priority_matrix():
    tasks = []
    with open(PLANNER_LOCATION, 'r') as f:
        tasks = f.readlines()

    for task in tasks:
        task_properties = task.strip().split(',')

def display_what_to_work_on():
    pass

@click.command()
@click.option('-a', '--add', default=False)
def main(add):
    print(add)
    display_priority_matrix()
    display_what_to_work_on()

if __name__ == '__main__':
    main()

