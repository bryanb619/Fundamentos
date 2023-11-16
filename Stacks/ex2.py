#Gerenciador de Telas:

#Crie uma stack para gerenciar as telas de um jogo. 
#A navegação dever ser feita com recurso a input, com uma opção fechar janela e para voltar à ultima

from collections import deque

action_history = deque()

screens_list = ["main menu", "settings", "game settings", "key bindings"]


def openWindow(current_window):
    action_history.append(current_window)
    print(action_history)

def CloseWindow():
    action_history.pop()
    print(action_history)



while True:

    print("""   
            Enter option:
          
            1 => Close window
            2 => Open window
            3 => Exit                       """)
    
    user_input = input("Enter option: ")

    if user_input == "1":
        CloseWindow()

    elif user_input == "2":

        print("Options are:", screens_list)

        if(len(action_history) == 0):
            print("Current window is:", "None")
        else:
            print("Current window is:", action_history[-1])

        second_input = input("Enter window name: ")

        if second_input in screens_list:
            openWindow(second_input)
        else:
            print("Window not found")
        #print("Current window is:", action_history[-1])
    
    else:
        print("Opção inválida")