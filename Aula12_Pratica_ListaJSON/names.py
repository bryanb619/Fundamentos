import random
import json


file_json_path = "D:\Projects\Exercises\FP\Aula12_Pratica_ListaJSON\list_of_names.json"
file_text_path = "Aula12_Pratica_ListaJSON\combos.txt"

names = ["John", "Jane", "Mary", "Michael", "Sarah", "William", "Linda", "David", "Elizabeth", "James"]

surnames = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", 
"Wilson"]


def save_json_file(file_path, names, surnames):
    
    try:
        dict = {"names": names, "surnames": surnames}

        print("Salvando arquivo JSON...")
        
        write_file = open(file_path, "w")
        json.dump(dict, write_file, indent=4)
        write_file.close()
                
    except Exception as error:
        print(error)

    
def generate_save_combo():
    

    #Escrever outra função, generate_combos(), que lê o ficheiro JSON, gera 10 combinações aleatórias de 
    # nome e apelido, sem repetições, e as salva num ficheiro de texto chamado combos.txt
    
    # le JSON
    read_json_file = open(file_json_path, "r")
    json_content = json.load(read_json_file)
    read_json_file.close()
    
    randomize = set() 
    
    
    write_text_file = open(file_text_path, "w")
    
    # 10 COMBINAÇÕES ALEATÓRIAS
    for i in range(10):    
        
        name = random.choice(json_content["names"])
        surnames = random.choice(json_content["surnames"])
        randomize.add(name + " " + surnames)
      
    write_text_file.write(randomize)
    
    
    
#save_json_file(file_json_path, names, surnames)
    
generate_save_combo()
    
    