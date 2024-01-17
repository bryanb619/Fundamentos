


def square_matrix_mult(m_a, m_b):
    
    ret = []
    dim = len(m_a)
    
    " Itera sobre as linhas da matriz resultante "
    for y in range(dim):
        
        # lista temporaria
        tmp = []
        
        " Itera sobre as colunas da matriz resultante "
        for x in range(dim):
            
            val = 0
            
            "Realiza o produto interno da matriz A com B"
            for k in range(dim):
                
                # valor é igual a Pos [y] [k] da matriz A * Pos [K][X] da matriz B
                val += m_a[y][k] * m_b[k][x]
                
            # dentro do loop X, adicionar valor obtido dentro do loop K
            tmp.append(val)
            
        # Dentro do loop Y, adicionar todos os resutlados do loop X
        ret.append(tmp)            
            
    return ret



m1 = [
    [1,2],
    [3,4]  
]

m2 = [
    [5,6],
    [7,8]
]

m3 = [
    [9,10],
    [11,12]
]


print(square_matrix_mult(m1,m3))