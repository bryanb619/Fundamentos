#Gerenciador de Telas:

#Crie uma stack para gerenciar as telas de um jogo. 
#A navegação dever ser feita com recurso a input, com uma opção fechar janela e para voltar à ultima

from collections import deque

action_history_stack = deque()

screens_list = ["main menu", "settings", "game settings", "key bindings"]


def openWindow(screen):
    if screen in screens_list:
        # adiciona a janela à stack
        action_history_stack.append(screen)
        # remove a janela da lista
        screens_list.remove(screen)
 

def close_current_window():

    # se a stack tiver elementos, ou seja, se a stack não estiver vazia 
    if action_history_stack: 

        # remove a janela da stack e adiciona-a à lista
        closed_screen = action_history_stack.pop()
        screens_list.append(closed_screen)

        # retorna mensagem com a janela fechada
        return "Closed",closed_screen
    
    # retorna mensagem se a stack estiver vazia
    return "No screens to close"
    


def window_manager():


    while True:

        print(f"Screens available are: {screens_list}")
        print("Choose screen to move in or close to go back. Type exit leave: ")
        
        # pedir input ao utilizador e fazer lower case dessa string
        choice_input = input("Enter option ").lower()

        # se o input for uma das janelas disponíveis na lista screens_list[], abre a janela
        if choice_input in screens_list:
            openWindow(choice_input)

        # se o input for close, fecha a janela
        elif choice_input == "close":
            print(close_current_window())

        # Fecha o programa
        elif choice_input == "exit":
            print("Thanks for using the program!")
            break

        # indica a janela atual
        if(action_history_stack):
            print(f"Current screen is {action_history_stack}")
            
        # indica se voltarmos ao inicio ou se nenhum ecrã estiver aberto
        else:
            print("No screens open")
    
window_manager()




    



    