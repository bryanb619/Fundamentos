def get_not_repeated(test_string):
    
    # ARRAY VAZIO para fazermos append posteriormente
    big_words = []
    
    # transformar em um array
    words = test_string.split()
    
    # iterar pelo array 
    # para cada palavra em words 
    for word in words:
        
        # se o len dessa palavra for >= 3 
        if len(word) >= 3:
            
            # append a big_wors
            big_words.append(word)


    return big_words
    

print(get_not_repeated("This is a test with a string"))



