# lista
my_list = [1, 2, 3, 4, 5, 6]


# Lambdas
even_lambda = lambda value: value % 2 == 0 
higher_than_3 = lambda value: value > 3


# 1. Crie uma função chamada filtro
def filtro(this_list, this_lambda):
    
    # temporary list
    temp_list = []
    # okay, ja estamos a passar os valores correctos
    for value in this_list:
        if this_lambda(value): # perfeito, estamos a chamar a função lambda e fazer um if!
             temp_list.append(value)# poderiamos chamar de forma diferentes, mas vamos testar

    # Retorne o valor
    return temp_list 
        

        
# vamos chamar a função
print(filtro(my_list, even_lambda))

print(filtro(my_list, higher_than_3))
