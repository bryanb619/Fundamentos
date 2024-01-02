""" Crie uma função recursiva chamada sum_int, que devolve a soma de todos os números inteiros menores ou 
iguais que o parametro """



# 1 

# função 

def sum_int(parameter):
    
    # checagem 
    if parameter == 0:
        return 0 

# temos de chamar de novo a função onde estamos e subtrair o parametro
# apos subtrair o parametro assim podemos chegar a uma checagem (if) para o codigo não correr eternamente.
    return parameter + sum_int(parameter -1)

print(sum_int(8))




