import random
from collections import deque

def random_events(this_list):
    random.shuffle(this_list)
    return this_list
    

def invert_events(this_list):
    my_stack = deque()

    for event in this_list:
        my_stack.append(event)
    

    my_stack.reverse()
    return my_stack


def add_events(inverted_events, events2_random):
    for event in events2_random:
        if event not in inverted_events:
            inverted_events.append(event)

    return inverted_events


def process_events(this_list):
    for event in this_list:
        print(f"Executing event: {event}")

    return "All events processed"


