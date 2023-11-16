from collections import deque

my_stack = deque()

items = ['Sword', 'Shield', 'Potion', 'Bow', 'Arrows', 'Axe', 'Armor']

my_stack.extend(items)

items_capacity = 5


def add_item(item):
    # append item to stack
    my_stack.append(item)
    print(my_stack)

def remove_item():
    # remove item from stack
    my_stack.pop()
    print(my_stack)

def out_of_bounds():

    print("Inventory is full")
    # print last item
    print("discarding:", my_stack[-1])
    my_stack.pop()
 
while True:

    print("Your invenrory items are:", my_stack)

    print("""
            1 => Add item
            2 => Remove item
            3 => Exit
""")

    user_input = input("Enter option: ")

    if user_input == "1":
        # check if lenght of stack is full
        if len(my_stack) > items_capacity:
            # call out of bounds function
            out_of_bounds()
        else:
            # ask for item and add it to stack
            selected_item = input("Enter item: ")
            selected_item = selected_item.capitalize()
            add_item(selected_item)

    # remove from stack
    elif user_input == "2":
        remove_item()
        
    elif user_input == "3":
        break
