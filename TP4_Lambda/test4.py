my_string = "This is a sentence and I want to count the words in it that are also in the given dictionary!"



def conta_tamanho_das_palavras(words):
    my_dict = {}
    words = words.split()

    for word in words:
        word = word.strip("!")
        my_dict = words
        
    print(my_dict.items())

    #print(words)
    
    #print(my_dict)
    


conta_tamanho_das_palavras(my_string)