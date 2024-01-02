import random

choices=[]

read_text = open(read_file_path + "texto.txt", "r")
all_lines = read_text.readlines()
for line in all_lines:
    choices.append(line)
    
tentativas = 5


while True:
    
    randomize = random.choice(choices)
    action = input(f"Ainda tem {tentativas} tentativas. Escolha uma palavra: ")
    
    if tentativas == 0:
        print("Game Over")
        break
    
    else:
        
        if action == randomize:
            print("You win")
            break
        else:
            tentativas -= 1
        
   
    