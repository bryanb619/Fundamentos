number_list = [1,2,3]
char_list = ["a","b","c"]


def interleave_lists(numbers, chars):
    
    # lista vazia
    new_list = []
    
    # Iterar sobre a listas simultaneamente
    for i in range (len(numbers)):

        # nova lista tem de fazer append 
        new_list.append(numbers[i])
        
        # se I for menor do que tamanho de chars, fazer append de chars no valor I
        if i < len(chars):
            new_list.append(chars[i])
      
      
    # retornar lista fora do for
    return new_list


print(interleave_lists(number_list, char_list))
        
        
    
        
        

        