import json

dict = {}
  
def carregar_dados():
    
    

    file = open('dados.txt', 'r')
    
    all_lines = file.readlines()
    
    for line in all_lines:
        line = line.strip(",.'")
        line = line.replace("\n", " ")
        line = line.split(";")
   
   
        for user in line:
            
            global dict
            dict = [line[0]] = {" ": line[1]}
            
        #print(dict)
        
        
        
        
        
def salvar_dados(dict):
    
    file = open('dados.json', 'w')
    
    json.dump(dict, file)
    
    file.close()

        

carregar_dados()
salvar_dados(dict)