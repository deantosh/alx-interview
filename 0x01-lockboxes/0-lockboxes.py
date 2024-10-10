#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is
numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.

Write a method that determines if all the boxes can be opened.

 - Prototype: def canUnlockAll(boxes)
 - boxes is a list of lists
 - A key with the same number as a box opens that box
 - You can assume all keys will be positive integers
 - There can be keys that do not have boxes
 - The first box boxes[0] is unlocked
 - Return True if all boxes can be opened, else return False
"""


def canUnlockAll(boxes):
    """ Check if all boxes can be unlocked """

    # Get the number of boxes
    num_boxes = len(boxes)

    # list of already opened boxes -- first box is unlocked by default
    opened_boxes = [0]

    # Keep track of keys we have
    keys = set(boxes[0])

    # Iterate through the keys we have
    while keys:
        key = keys.pop()
        if key < num_boxes and key not in opened_boxes:
            opened_boxes.append(key)
            keys.update(boxes[key])

    # Return True if all boxes are opened
    return len(opened_boxes) == num_boxes
