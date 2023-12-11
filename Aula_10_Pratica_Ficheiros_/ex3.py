import json
# ex 1
filePath ="D:\\Projects\Exercises\FP\Aula_10_Pratica_Ficheiros_"

JsonPath ="D:\\Projects\Exercises\FP\Aula_10_Pratica_Ficheiros_"

words = ""

def load_characters():
    
    dict = {}
    
    file = open (f"{filePath}/" + "cha.txt" , "r")
    
    all_lines = file.readlines()
    
    for line in all_lines:
    
        name, classe, streght, intelligence, agility = line.strip().split(";")
        
        if name not in dict:
            dict[name] = {classe, streght, intelligence, agility} 
            
    file.close()
    save_characters(dict)
            
    

def save_characters(char_dict):

    file = open (filePath + "/" + "cha.json" , "w")
    
    file.write(json.dumps(char_dict))
    
    file.close()


load_characters() = "D:\Projects\Exercises\FP\Aula_10_Pratica_Ficheiros_\cha.json"

words = ""

def load_characters():
    
    dict = {}
    
    file = open (f"{filePath}/" + "cha.txt" , "r")
    
    all_lines = file.readlines()
    
    for line in all_lines:
    
        name, classe, streght, intelligence, agility = line.strip().split(";")
        
        if name not in dict:
            dict[name] = {classe, streght, intelligence, agility} 
            
    file.close()
    save_characters(dict)
            
    

def save_characters(char_dict):
    
    print(char_dict)

    file = open ( , "w")

    data = json.dumps(char_dict)
    
    


load_characters()