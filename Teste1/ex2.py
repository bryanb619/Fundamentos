

"""
Crie uma função sum_pairs, que recebe uma lista com uma quantidade par de elementos e devolva uma lista 
com metade dos elementos, em que os elementos são a soma dos dois elementos consecutivos na lista original. Se 
a lista original não tiver um número par de elementos, a função deve devolver uma lista vazia
"""

passList = [1,2,3,4,5,6,7]

def sum_pairs(someList):
    
    new_list = []
    
    # checar se lista tem comprimento/tamanho par
    if len(someList) %2 == 0:
        
        # novo array para guardar as somas
        new_list = []
        
        # iterar sobre a lista 
        "0 = Start"
        "len(someList) = Stop"
        "2 = step, a cada 2 elementos"
        for i in range(0, len(someList), 2):
            # usar o array local
            # adicionar posição inicial e somar 1 na segunda posição
            # Isto, porque através da iteração não temos acesso direto ao segundo elemento 
            new_list.append(someList[i] + someList[i+1])
            
        return new_list
            
            
            
    else:
        return[]
    
    
print(sum_pairs(passList))

