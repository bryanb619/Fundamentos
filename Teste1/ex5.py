def get_unique(my_string):
    
    # criamos dicionario como sugerido no enunciado
    word_count = {}
    # removemos single quotes
    words = my_string.split(' ')
    
    # em cada elemento de words
    for word in words:
        
        # se o tamanho desse elemento >= 3
        if len(word) >= 3:
            
            # se a palavra ja estiver no dicionário adicionar 1 valor
            if (word in word_count):
                word_count[word] +=1
                
            # caso contrário é igual a 1 o numero de repetições
            else:
                word_count[word] = 1
    
    
    # lista para devolver
    new_list = []    
    
    # para cada palavra na contagem de word_count ( o nosso dicionario )
    for word, count in word_count.items():
        # se a contagem desse elemento for igual a 1 no dicionario, fazer append na lista
        if(count == 1):
            new_list.append(word)
            
    return new_list


print(get_unique("I have the word string repeated in this string at least twice"))