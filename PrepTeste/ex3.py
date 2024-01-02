def sort_modified(numbers, function):
    
    # "n" recebe o tamanho de numbers, a nossa lista
    n = len(numbers)
    
    
    # itera sobre a lista inteira pelo tamanho de "n"
    for i in range(n):
        
        # Itera sobre a parte indiferenciada da lista (unsorted)
        for j in range( n - i - 1):
            
            #  checa se o elemento no indice J e J+1 estão na posição correta
            # se não estiverem no indice certo são trocados
            if not function (numbers[j], numbers[j+1]):
                
                # faz a troca de posições
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                
    # retorna a lista de forma ordenada
    return numbers
    
    
    
values = [3,1,4,1,5,9,2,6,5,3]

""" 
    Função que aceita 2 paremtros:
    - lista
    - comparação
    
"""
sort_modified(values, lambda a,b: a < b ) # a < b, porque compara o valor a com b, se a menor que b, correto

print(values)

