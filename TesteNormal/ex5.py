""" 5. [3v] Crie uma função chamada get_pairs, que recebe duas listas e
retorna uma lista com todos os pares passíveis de serem 
criados com elementos da primeira e da segunda lista
"""

""" União de pares de cada Lista

    # Para cada elemento i da lista A,o loop interno 
    percorre cada elemento j da Lista B.

    1. Percorre cada elemento i da Lista A
    
    2. Percorre cada elemento j da Lista B
    
    3. Para cada par de elementos (i,j) 
       São então adicionados a uma lista em forma de tuplos

    param l_a: Lista A
    param l_b: Lista B
"""
def get_pairs(l_a,l_b):
    
    ret = []
    
    # 1. 
    for i in l_a:
        # 2. 
        for j in l_b:
            
            # 3.
            ret.append((i,j))
            
    return ret


print(get_pairs(["a","b","c"], [1,2,3,4]))
print("""
--------------------------------
 """)


