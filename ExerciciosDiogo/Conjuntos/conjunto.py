frases = [
 "Python é uma linguagem poderosa.",
 "Programação é divertida.",
 "Desenvolvimento web é incrível.",
 "Python tem uma comunidade ativa.",
 "Aprender programação é essencial nos dias de hoje."
]

unwanted_chars = [".", ",", "!", "?"]


# Função que encontra as palavras únicas
def encontrar_palavras_unicas(frases_a_analisar):

    #cria um conjunto vazio, se não fizermos isso, Python vai criar um dicionário
    my_set = set() 

    # junta todas as frases numa string e fazemos lowercase de tudo
    my_sting = "".join(frases_a_analisar).lower() 

    # para cada caracter indesejado, substitui por um espaço
    for char in unwanted_chars:
        my_sting = my_sting.replace(char, " ")

    # divide a string e converte-a novamente numa lista de palavras
    my_sting = my_sting.split()

    # para cada palavra na lista, se a palavra aparecer apenas uma vez, adiciona-a ao conjunto
    for word in my_sting:
        # se o count for igual a 1, adiciona a palavra ao conjunto
        if word.count(word) == 1:
            # adiciona a palavra ao conjunto
            my_set.add(word)

    # retorna o conjunto
    return my_set
    
    

palavras_unicas = encontrar_palavras_unicas(frases)

print("Palavras únicas: ", palavras_unicas)