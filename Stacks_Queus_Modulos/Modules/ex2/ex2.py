from collections import deque
from QueueManipulator import QueueManipulator

list = ["helmet","boots","gloves","armor","pants"]

queeu = deque()
queeu.extend(list)



print(QueueManipulator.move_to_end(queeu))

#move_to_end(queeu)







