"""
3. [2v] Dada uma lista de listas com números inteiros (como numa grelha com N linhas e M colunas), crie duas funções sum_column
e sum_row que some todos os valores numa coluna e numa linha respectivamente. As funções devem retornar zero se a coluna 
ou a linha não existir.

"""


""" soma todos os elementos de uma coluna de uma matriz:

    1. Se a coluna não existir, retornar 0 (inteiro zero)
    
    2. Iterar sobre a matriz e declarar uma variável para guardar a soma dos elementos da coluna:
        Este loop é feito com o tamanho da matriz
        
    3. col_sum é igual a soma da matriz na linha i e coluna col (ou seja, o elemento da coluna col na linha i)
    
    4. Retornar o valor da soma
    
"""
def sum_column(m, col):
    
    # 1.
    if col > len(m[0]):
        return 0
    
    # 2.
    col_sum = 0
    for i in range(len(m)):
        
        # 3.
        col_sum += m[i][col]
     
    # 4. 
    return col_sum
    
    
    
""" soma todos os elementos de uma linha de uma matriz:
    
    1. Se a linha não existir, retornar 0 (inteiro zero)
    
    2. Iterar sobre a matriz (sobre as linhas, por causa de um loop for externo):
    
    -   1.a) Se i for igual ao número da linha, retornar a soma dos elementos da linha i no loop em questão
    -   1.b) retornar o valor da soma
    
param m: matriz
param row: linha da matriz a somar os elementos

"""
def sum_row(m, row):
    
    # 1.
    if row > len(m):
        return 0
 
    # 2.
    for i in range(len(m)):
        
        # 2.a
        if i == row:
            # 2.b
            return sum(m[i])
        


grid = [
    [3,4,6],
    [4,5,8],
    [1,2,3],
    [4,5,6]
]


""" Testes """

" sum_row "
# deve retornar 6
print("Soma de linha: ")
print (sum_row(grid , 2))

# deve retornar 0, porque a linha 8 não existe
#print (sum_row(grid , 8))

" sum_column "
print("Soma de coluna: ")
print(sum_column(grid , 2)) # deve retornar 23