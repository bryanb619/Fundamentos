"""
[3v] Crie uma função to_grid que transforme uma lista de números numa lista de listas com N por M elementos, fornecidos como 
parametros. A função deve verificar se a lista tem números suficientes para criar a lista de listas antes de fazer o processo. Se não 
tiver, deve retornar uma lista vazia

"""



def to_grid(some_list, n,m):
    
    # se a lista for menor do que n*m, retorna uma lista vazia
    if len(some_list) < n*m:
        return []
    
    else:
        
        ret = []
        
        # itera sobre as linhas
        for i in range(n):
            tmp = []
            
            # itera sobre as colunas
            for j in range(m):
                
                # adiciona o elemento na posição i*m+j
                tmp.append(some_list[i*m+j])
                
            # adiciona a linha na lista de retorno
            ret.append(tmp)
            
        return ret

print(to_grid([1,2,3,4,5,6,7,8,9],3,3))
#-------------------------------------------------------------#


"Versão alternativa"

"""
    1. checar se a lista tem tamanho para podermos fazer uma matriz (lista de listas com N por M elementos)
        Retornar lista vazia
        
    - Criar listas vazias
    
    2. For com alcance em N -> É uma iteração sobre as linhas
    3. For interno com alcance em M -> É uma iteração sobre as colunas
    4. Adicionar a lista temp a seguinte equação:
        i*m+j
        
       - Devemos buscar dentro do loop j (loop interno) a posição dada pela equação acima
       - Adicionar posição obtida pela equação a lista temp a cada loop de j
        
    5. Adicionar a lista temp obtida em cada loop de i a lista ret
    6. retornar a lista a chamada de função
    

"""
def to_grid2(list, n,m):
    
    # 1. 
    if len(list) < n*m:
        return []
    
    # -
    
    ret = []
    
    
    # 2.
    for i in range(n):
        
        # -
        temp = [] # deve estar dentro loop!!!! Consultar linha 92
        
        # 3.
        for j in range(m):
            
            # 4.
            temp.append(list[i*m+j])
            
        # 5.
        ret.append(temp)
        
    # 6.
    return ret
        
print(to_grid2([1,2,3,4,5,6,7,8,9],3,3))
        

""" temp dentro de loop

    Deve estar dentro porque, a lista é utilizada para guardar apenas 1 linha
    A cada loop deve estar uma nova lista para cada iteração(loop) do programa
    
    Caso temp estivesse fora, isto iria acontecer...
    
    - Não seria reinicializado e como resultado iria incluir o resultado anteriores

    ex:
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    
    Portanto é possível concluir que fez uma matrix com 3 rows, mas incluiu os elementos de operações anteriores.
    
"""

print("""
--------------------------------
 """)