frases = [
 "Python é uma linguagem poderosa.",
 "Programação é divertida.",
 "Desenvolvimento web é incrível.",
 "Python tem uma comunidade ativa.",
 "Aprender programação é essencial nos dias de hoje."
]

unwanted_chars = [".", ",", "!", "?"]


def encontrar_palavras_unicas(frases_a_analisar):
    my_set = {}

    #frases_a_analisar = frases_a_analisar.lower().strip()
    #frases_a_analisar.split()

    for frase in frases_a_analisar:
        #frase = frase.replace(unwanted_chars, "")
        if frase in frases_a_analisar:
            frases_a_analisar.remove(frase)
        else:
            my_set.add(frase)

    return my_set
           
    


palavras_unicas = encontrar_palavras_unicas(frases)

print("Palavras únicas: ", palavras_unicas)