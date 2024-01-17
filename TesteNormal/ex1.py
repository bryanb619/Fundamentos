""" 
1. Crie uma função chamada mul_all, que recebe uma lista de números e 
retorne a multiplicação do quadrado de todos os 
números. Se a lista estiver vazia, a função deve devolver zero

"""

" Função que recebe uma lista de números e retorna a multiplicação do quadrado de todos os números "
def mul_all(some_list):
    
    # verifica se a lista tem mais de um elemento!
    if len(some_list) >= 1:
        
        # result começa em 1 para que o resultado não seja 0...
        result = 1
        
        # iterar sobre a lista a procura de números
        for num in some_list:
            
            # elevar o número ao quadrado e multiplicar por result
            result *= num ** 2 #  Ou  "result = result * num ** 2"
            
        return result
    
    else:
        empty_list = []
        return empty_list
  
  
print(mul_all([1,2,3,4,5]))
