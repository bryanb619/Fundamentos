#Histórico de Ações do Jogador:

#Implemente uma stack para armazenar as ações de um jogador . 
#Cada ação é uma string descrevendo o movimento. 
#Implemente métodos - undo_last_action() e add_new_action().


from collections import deque

my_stack = deque()

actions_history =  ["move pawn", "take card", "play dice", "capture enemy"]

my_stack.extend(actions_history)


def add_new_action(my_action):
    my_stack.append(my_action)
    print(my_stack)

def undo_last_action():
    my_stack.pop()
    print(my_stack)



while True:

    print("""   
                1 => Remove last action
                2 => Add new action
                3 => for exit  """)
    

    my_input = input("Digite uma opção: ")


    if my_input == "1":
        undo_last_action()

    elif my_input == "2":
        my_action = input("Digite a ação: ")
        my_action = my_action.lower()
        add_new_action(my_action)

    elif my_input == "3":
        break










