# Sistema gerencioamente de animações

from collections import deque

#animation_event = ["attack","move","pick up item"]

animation_queue = deque()


def add_animation_event(event):
    animation_queue.appendleft(event)
    print(f"Add animation: {event}")

def execute_animations():
    while len(animation_queue) > 0:
        print("Executing animation:",animation_queue.pop())
    


while True:
    print("Type the animations you want to execute. Type \n´done\n' to execute: ")

    user_input = input("Type action: ")

    if user_input == "done":
        execute_animations()
    else:
        add_animation_event(user_input)
        print(animation_queue)
        continue