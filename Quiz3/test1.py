
def carregar_dados():
    
    
    dict = {}
    
    file = open('dados.txt', 'r')
    
    all_lines = file.readlines()
    
    for line in all_lines:
        line = line.strip(",.'")
        line = line.replace("\n", " ")
        line = line.split(";")
   
   
        for user in line:
            dict = [line[0]] = {line[1]}
            
        print(dict)

        

carregar_dados()
