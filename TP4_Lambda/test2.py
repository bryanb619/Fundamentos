sentence = "This is a sentence and i want to count the words in it that are also in the given dictionary"

words = {"sentence","want","in"}

def conta_palvras(my_str, my_set = set() ):# apaguei para nao dar erro

    # temos de criar um dicionário vazio, ou seja, inicializar o dicionário
    my_dict = {} # criamos um dicionario vazio

    # vamos processar a nossa string

    my_str = my_str.lower().strip() 

    # temos de fazer split da nossa string, para a tratar como um array de palavras
    my_str = my_str.split()


    # ja entendi a logica :)
    # para cada palavra na minha string
    for word in my_str:
        # se a palavra estiver no set, ou seja
        if word in my_set:
            # se word estiver em dicionario, adicionar 1
            # isto para mim é um bocado confuso,porque estamos a checar ja no dicionario
            if word in my_dict:
                my_dict[word] += 1
            # else = 1
            else:
                my_dict[word] = 1
    
    return my_dict
       
            # hmm,acho que agora vai porra
            # nos [x] o nosso x é a palavra, no caso do nosso dicionário é a key!
            # a seguir é o valor, ou seja, o numero de vezes que aparece, que é o value! thanks chat gpt

    # sempre que um exercicio fala numa função devolvemos um valor, assumimos que é um return ou um print tbm serve
    # okay, vamos fazer o return
    #return my_dict 
 

# vamos ver se funciona!! :)
print(conta_palvras(sentence, words)) # pronto, ja estamos a enviar a string e o set!

#conta_palvras(sentence, words)


    
