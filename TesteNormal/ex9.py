"""
[1v] Crie uma função chamada process, que recebe uma lista e uma função lambda e retorna uma lista com todos os elementos 
da lista original processados por essa função.
"""

""" Processamento de lista

    1. O retorna uma nova lista onde cada elemento é 
    o resultado da função lambda aplicada ao elemento da lista original
    
    Portanto essa linha (10) chama a função lambda e processa a lista de acordo
    com a instrução lambda passada na chamada da função process
"""
def process(list, function):
    
    # 1. 
    return [function(x) for x in list]

    

print(process(["abc","def","ghi"], lambda x: x * 2))

print(process(["abc","defdef","ghij"], lambda x: len(x)))



"EXTRA"

"""
Como chamar lambda com mais do que um argumento
e retornar o resultado da função lambda

"""
def process_multiple(a,y, func):
    
    return func(a,y)


add = lambda a,b: a+b
mul = lambda a,b: a*b

print(process_multiple(5,2,add))
print(process_multiple(3,3, mul))

print("""
--------------------------------
 """)

#print(process_multiple(5,2,lambda a,b: a+b))