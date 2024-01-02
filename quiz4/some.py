# Pergunte ao utilizador quantos números ele deseja inserir.
# Peça ao utilizador para inserir esses números um por um.
# Calcule a média dos números inseridos.
# Exiba a média para o utilizador.


import json

times_run = 0

number_list = []


my_dict = {"times_run": times_run,
           "number_list": number_list}

while True:
        
    try:
        
        i = 0
        
        n_action = input("Quantos números deseja inserir?")
        #print(n_action) # test
        
        times_run += 1
        
        while i < int(n_action):
            
            i+=1
            
            insert_number = input(f"{i} Insira um número real: ")
            
            number_list.append(int(insert_number))
   
   
        mySum = sum(number_list)/len(number_list)
        
        print(f"A média é {mySum}")
        
        
        file = open("numbers.json", "wt")
        json.dumps(my_dict)
        
        
        file.close()
        
    except ValueError:
        print("Insira um número inteiro!")
    
        
    finally:
        print(f"O programa! já foi executado {times_run} vez(es)")



    
    
    
