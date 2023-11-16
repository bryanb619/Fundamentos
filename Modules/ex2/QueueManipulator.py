from collections import deque



def move_to_end(my_queue):
    for i in range(len(my_queue)):
        my_queue.append(my_queue.popleft())
    return my_queue

def check_empty(my_queue):
    
    if my_queue.is_empty():
        return True
    else:
        return False
    
