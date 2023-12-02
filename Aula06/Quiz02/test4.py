import random

# função
def compute_hist(numero_de_lancamentos, funcao_aleatoria):
    # declarar dicionário vazio
    my_dict = {}

    # loop para checar o numero de lançamentos
    for i in range(numero_de_lancamentos):

        # chamar a função aleatória 
        resultado = funcao_aleatoria()

        if resultado in my_dict:
            # converter para int, o resultado
            my_dict[int(resultado)] += 1
        else:
            # fazer int a mesma
            my_dict[int(resultado)] = 1

    # retornar dict
    return my_dict
    

print(compute_hist(10, lambda : random.randint(1, 7)))
print(compute_hist(1000, lambda : random.randint(1, 7)))
print(compute_hist(1000, lambda : random.gauss(4, 0.8)))

# Resultado é algo parecido com isto:
# {1: 2, 7: 1, 3: 2, 4: 1, 2: 1, 5: 3}
# {6: 141, 2: 150, 7: 145, 1: 138, 5: 129, 3: 133, 4: 164}
# {4: 422, 5: 98, 3: 366, 2: 98, 1: 8, 6: 8}