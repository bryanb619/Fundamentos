filepath = "D:\Projects\Exercises\FP\Aula9_Pratica_FicheirosJSON"

myInput = input("type the filename without extension: ")

myInput = myInput.lower()
myInput = filepath + "/" + myInput + ".txt"

wordDict= {}


file = open( myInput, "rt")

all_lines = file.readlines()

file.close()

# Exercício anteror ^
# ----------------------------------

"""
    1. For loop to read all lines
    2. Por linha em todas a linhas
    3. fazer split = transformar em lista
    4. Para cada elemento da lista em words
    5. remover indesejados
    6. se a extenão da palavra for maior que 7
    7. e se não estiver no dicionário
    8. adicionar ao dicionário
    

"""
# 1
for line in all_lines:
    
    # 2
    for line in all_lines:
        
        # 3
        words = line.split() 
        
        # 4
        for word in words:
            # 5
            word = word.strip(";,!?- ").lower()
            
            # 6
            if len(word) > 7:
                
                # 7
                if word not in wordDict:
                    
                    # 8
                    wordDict[word] = len(word)
        
print(wordDict)
        
    
    





    

