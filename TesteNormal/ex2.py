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