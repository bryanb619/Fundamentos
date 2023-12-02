from collections import deque

"""
Exemplo de operação:

1. Inserir operação
2. Listar operações
3. Undo
4. Sair
"""
# declarar stack
my_stack = deque()

def insert_operation(action):
    my_stack.append(action)


def list_operations():
    if my_stack:
        print(f"Operações: {my_stack}")
    else:
        print("Sem operações")

def undo_operation():
    if my_stack:
        my_stack.pop()
    else:
        print("Sem operação para undo")


while True:

    print("""
    1. Inserir operação
    2. Listar operações
    3. Undo
    4. Sair
    """ )

    
    user_input = input("Escolha uma opção: ")

    if user_input == "1":
        user_operation = input("Digite a operação: ")
        insert_operation(user_operation)

    elif user_input == "2":
        list_operations()

    elif user_input == "3":
        undo_operation()

    elif user_input == "4":
        print("Obrigado por usar o programa!")
        break

    

