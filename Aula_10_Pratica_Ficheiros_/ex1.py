# ex 1
filePath ="D:\\Projects\Exercises\FP\Aula_10_Pratica_Ficheiros_"

words = ""

def load_characters():
    
    dict = {}
    
    file = open (f"{filePath}/" + "cha.txt" , "r")
    
    all_lines = file.readlines()
    
    file.close()
    
    global words
    
    for line in all_lines:
    
        name, classe, streght, intelligence, agility = line.strip().split(";")
        
        if name not in dict:
            dict[name] = {classe, streght, intelligence, agility} 
            
    return dict
 
    
    
        
print(load_characters())
    
    