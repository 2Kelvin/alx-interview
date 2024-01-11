#!/usr/bin/python3
'''Lockboxes interview challenge'''


def canUnlockAll(boxes):
    '''Checking if all boxes can be unlocked'''

    for k in range(1, len(boxes)):
        state = False
        for i in range(len(boxes)):
            if k in boxes[i] and i != k:
                state = True
                break
        if not state:
            return False

    return True
