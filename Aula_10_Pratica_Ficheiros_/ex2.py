import json
# ex 1
filePath ="D:\\Projects\Exercises\FP\Aula_10_Pratica_Ficheiros_"


dict = {}


def save_characters(char_dict):

    file = open ("stats.json" , "w")

    json.dump(char_dict, file)
    
    file.close()
    
    

def load_characters():
    

    file = open ("cha.txt" , "r")
    
    all_lines = file.readlines()
    
    for line in all_lines:
    
        name, classe, streght, intelligence, agility = line.strip().split(";")
        
        if name not in dict:
            dict [name] = {"Class": classe, "Streght": streght, "Inteligence":intelligence, "Agility":agility} 
    
         
    file.close() 
    return dict

            

#load_characters()


save_characters(load_characters())
