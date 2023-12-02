# test 6
from collections import deque


my_queue = deque()

# add events to the list
def adicionar_evento(my_string):

    my_queue.appendleft(my_string)
    return my_queue

# processar evento
def processar_evento():

    # if queue is not empty
    if my_queue:
        return my_queue.pop()
    # sem eventos para processar
    else:
        return "No event to process"
    
# adicionar eventos
print(adicionar_evento("game over"))
print(adicionar_evento("Game start"))

print(processar_evento())
print(processar_evento())

