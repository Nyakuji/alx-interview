#!/usr/bin/python3
"""Lockboxes"""
from collections import deque


def canUnlockAll(boxes):
    """
    Method that determines if
    all the boxes can be opened
    """
    n = len(boxes)
    if n == 0:
        return True

    Visited = set()
    queue = deque([0])  # Start with the first box
    # Mark the first box as visited
    Visited.add(0)

    while queue:
        current_box = queue.popleft()
        # Explore the current box
        for key in boxes[current_box]:
            if key not in Visited and key < n:
                queue.append(key)
                Visited.add(key)

    # If all the boxes have been visited
    return len(Visited) == n
