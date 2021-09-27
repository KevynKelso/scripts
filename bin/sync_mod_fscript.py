#!/usr/bin/env python3

import json
import sys
import random




def get_random_state():
    number = random.randint(0, 100)
    if number < 40:
        return 0
    if number < 60:
        return 1
    if number < 80:
        return 2
    if number <= 90:
        return 3
    if number <= 100:
        return 4


def randomize_actions(data):
    actions = data['actions']
    count = 0
    state = get_random_state()

# 0 is normal, no change
# 1 is 0 - 50
# 2 is 50 - 100
# 3 is 60 - 80
# 4 is 70 - 100

    for i, action in enumerate(actions):
        if count == 20:
            count = 0
            state = get_random_state()
    
        if state == 0:
            count += 1
            continue

        if state == 1 and action['pos'] >= 90:
            count += 1
            action['pos'] = 60
            actions[i] = action
            continue

        if state == 2 and action['pos'] <= 10:
            count += 1
            action['pos'] = 40
            actions[i] = action
            continue

        if state == 3 and action['pos'] >= 90:
            count += 1
            action['pos'] = 80
            actions[i] = action
            continue

        if state == 3 and action['pos'] <= 10:
            count += 1
            action['pos'] = 40
            actions[i] = action
            continue

        if state == 4 and action['pos'] <= 10:
            count += 1
            action['pos'] = 70
            actions[i] = action
            continue

        if state == 4 and action['pos'] >= 90:
            count += 1
            action['pos'] = 100
            actions[i] = action
            continue

    return actions


def read_funscript(file_path):
    data = {}
    with open(file_path, 'r') as f:
        data = json.load(f)
        data['actions'] = randomize_actions(data)

    with open(f'newfs.funscript', 'w') as f:
        f.write(json.dumps(data))


def main(args):
    read_funscript(args[1])


if __name__ == '__main__':
    main(sys.argv)

