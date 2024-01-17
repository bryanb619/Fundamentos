
""" Soma de elementos da Lista

    1. Obter o tamanho da lista
    
    2.1 Se o tamanho da lista for par:
    
    -   2.1.1 Iterar sobre a lista, começando em 0, parando em tamanho "l" e com passo 2 unidades
    -   2.1.2 Somar o elemento atual com o próximo elemento da lista
        
    2.2 Se o tamanho da lista for ímpar:
        2.2.1 Iterar sobre a lista, começando em 0, parando em l-1 (porque devemos parar antes !) com passo 2 unidades
        
    
"""

def sum_pairs(some_list):
    
    # 1.
    l = len(some_list)
    
    # 2.1
    if l %2 == 0:
        
        ret = [] # lista de retorno
        
        #2.1.1
        for i in range(0, l, 2):
            # 2.1.2
            ret.append(some_list[i] + some_list[i+1])
            
        return ret
            
    # 2.2
    else :
        
        odd_ret = [] # lista de retorno ímpar
        
        for i in range(0, l -1, 2):
            ret.append(some_list[i] + some_list[i+1])
        odd_ret.append(some_list[-1])
        
        return odd_ret
        

print(sum_pairs([1,2,3,4,5,6]))