"""
3. [2v] Dada uma lista de listas com números inteiros (como numa grelha com N linhas e M colunas), crie duas funções sum_column
e sum_row que some todos os valores numa coluna e numa linha respectivamente. As funções devem retornar zero se a coluna 
ou a linha não existir.

"""


""" soma todos os elementos de uma coluna de uma matriz:

    1. Se a coluna não existir, retornar 0 (inteiro zero)  
    
    OBS :> if you want to check if col is out of bounds 
    (i.e., if it's not a valid column index), 
    you should use if col >= len(m[0]). 
    This condition will return True if col is greater than or equal to the number of columns, 
    which means that col is not a valid column index.
    
    2. Iterar sobre a matriz e declarar uma variável para guardar a soma dos elementos da coluna:
        Este loop é feito com o tamanho da matriz
        
    3. col_sum é igual a soma da matriz na linha i e coluna col (ou seja, o elemento da coluna col na linha i)
    
    4. Retornar o valor da soma
    
"""
def sum_column(m, col):
    
    # 1.
    if col >= len(m[0]):
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
        
        num = 0 
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
print("Soma de coluna:  'Versão 1'")
print(sum_column(grid , 2)) # deve retornar 23
#---------------------------------------------------------#


" Versão alternativa "


""" Esta Versão certifica que tudo esta correto dentro da matriz (Certifica que existe o numero colunas apropriado em cada linha)

    1. variável local para incrementação
    
    2. Iteração com alcance máximo em tamanho da matriz
    3 e 4. 
    - Se a coluna não existir, continuar e incrementar sum_total com 0, (0+0 = 0)
    - Se a coluna existir incrementar com valor solicitado em matriz[posição de linha] e [posição de coluna]
    
    5. retornar a soma seja qual for o caso... 

"""
def sum_column2(m, col):

    # 1.
    sum_total = 0
    
    # 2. 
    for i in range(len(m)):
        
        # 3.
        if col >= len(m[i]):
            continue
        # 4.
        sum_total += m[i][col]

    # 5. 
    return sum_total
        
     

""" 
    1.Verficar se a linha existe
    
    2. criar uma variável para guardar a soma dos elementos da linha
    
    3. Iterar sobre a lista na posição param: row (ou seja, apenas buscar elementos na linha pedida)
    4. Somar entao a cada loop o numero obtido na linha(row)
    5. Retornar o total 
    
param: m: matrix
param: row: row 
"""
def sum_row2(m, row):
    
    # 1.
    if row > len(m):
        return 0
    
    # 2. 
    total_sum = 0

    # 3. 
    for number in m[row]:
        # 4.
        total_sum += number
            
    return total_sum




" sum_column "
print("Soma de coluna:  'Versão 2'")
print(sum_column2(grid , 2)) # deve retornar 23
    
print("Soma de linha: 'Versão 2'")
print(sum_row2(grid , 2))





        
    
