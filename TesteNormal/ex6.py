""" 6. [4v] Crie uma função chamada count_words, que recebe uma string e devolve um dicionário cujos entradas são o número de 
ocorrências das várias palavras que compõem a string.

"""


""" Contagem de palavras

    1. Transformar a string em uma lista de palavras para podermos usar um for
    
    2. Iterar sobre a lista de palavras:
    
    3. Se a palavra já estiver no dicionário, incrementa o valor da chave (chave sendo a palavra)
    
    4. Caso contrário, adiciona a palavra no dicionário com o valor 1
    
    5. Retorna o dicionário
    
    param: some_string -> string a ser contada
"""
def count_words(some_string):
    
    my_dict = {}
    
    # 1.
    words = some_string.split()
    
    
    # 2.
    for word in words:
        
        if word in my_dict:
            
            # 3.
            my_dict[word] += 1 # incrementa o valor da chave (chave sendo a palavra)
            
        else:
            # 4.
            my_dict[word] = 1  
            
    # 5.
    return my_dict 


print(count_words("This is a string that has a lot of words that have to be counted"))
print("""
--------------------------------
 """)
    
    



