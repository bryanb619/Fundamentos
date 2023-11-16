from collections import deque

queue = deque()



def add_event(event):
    queue.appendleft(event)

def execute_events(execute_all):

    if execute_all:
        print(queue)
        i = 0
        print("executing all events") # usar while loop e pop
        for i in range(len(queue)):
            print(queue[i])
            i += 1
    else:
        print("Event is:",queue.pop())

        
        queue.pop()
  
 

add_event("attack")
add_event("move")
add_event("pick up item")

execute_events(True)


    

