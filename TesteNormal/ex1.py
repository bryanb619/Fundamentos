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
        return 0
  
#print(mul_all([1,2,3,4,5]))

#------------------------------------------------------------------------------------------------------------#

"""  Alternativa 

    1. Verificar se lista é menor que 1
    -   1.1 Caso sim, retornar int 0
    
    2. criar variável local com valor 1 (para não zerar multiplicações)
    3. Usar for para aceder a elementos da lista
    4. Fazer calculo (multiplicação ao quadrado do número)
    5. retornar valor de result para a chamada de função!
    
 
"""
def mul_all2(list):
    
    # 1.
    if len(list) < 1:
        # 1.1
        return 0
    # ------------------

    # 2. 
    result = 1
    
    # 3.
    for num in list:
        # 4.
        result *= num** 2
    # --------------------
        
    return result


print(mul_all2([1,2,3,4,5]))

        
        

