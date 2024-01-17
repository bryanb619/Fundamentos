""" Crie uma função sum_pairs, que recebe uma lista com uma quantidade par de elementos e devolva uma lista com metade 
dos elementos, em que os elementos são a soma dos dois elementos consecutivos na lista original. Se a lista original não tiver um 
número par de elementos, a função deve somar os pares possíveis.
"""




""" Soma de elementos da Lista

    1. Obter o tamanho da lista
    
    2.1 Se o tamanho da lista for par:
    
    -   2.1.1 Iterar sobre a lista, começando em 0, parando em tamanho "l" e com passo 2 unidades
    -   2.1.2 Somar o elemento atual com o próximo elemento da lista
    -   2.1.3 Retorna a lista de retorno
        
    2.2 Caso não seja par:
    -    2.2.1 Iterar sobre a lista, começando em 0, parando em l-1 (porque devemos parar antes de chegar ao fim!) com passo de 2 unidades
    -    2.2.2 Somar o elemento atual com o próximo elemento da lista   
    -    2.2.3 Acessa o ultimo elemento da lista e adiciona a lista de retorno (o que sobrou!)
    -    2.2.4 Retorna a lista de retorno
        
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
            
        # 2.1.3
        return ret
            
    # 2.2
    else :
        
        odd_ret = [] # lista de retorno ímpar
        
        # 2.2.1
        for i in range(0, l -1, 2):
            # 2.2.2
            ret.append(some_list[i] + some_list[i+1])
        # 2.2.3
        odd_ret.append(some_list[-1])
        
        return odd_ret
        

print(sum_pairs([1,2,3,4,5,6]))