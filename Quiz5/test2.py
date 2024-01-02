
read_file_path = "D:\Projects\Exercises\FP\Quiz5\\"


try: 
    
    """
    Leia o conteúdo do ficheiro "texto.txt".
    Conte o número total de palavras no ficheiro.
    Conte o número total de caracteres (incluindo espaços) no ficheiro.
    Conte o número total de linhas no ficheiro.
    Encontre a palavra mais longa no ficheiro (se houver empate, usa a última que encontrares).
    Crie um novo ficheiro chamado "estatisticas.txt" e escreve as seguintes informações nele
    """
    
    read_text = open(read_file_path + "texto.txt", "r")
    all_lines = read_text.readlines()
    all_chars = read_text.readlines()   
    all_lines = [line.strip() for line in all_lines]
    
    palavras =[]
    
    read_text.close()
    
    # Palavras
    words = all_lines
    words = [line.split() for line in all_lines]
    
    
    for word in words:
        for newWord in word:
            palavras.append(newWord)
    
    # Caracteres
    caracteres = []
    for char in all_chars:
        caracteres.append(char)
        
    
    #caracteres = str(len(all_chars))
    
    # linha
    linhas = all_lines
    linhas = len(all_lines)
    

    # Palavra mais longa
    longWord = ""
    for word in palavras:
        if len(word) > len(longWord):
            longWord = word
    
    
    """ Número total de palavras: 17
        Número total de caracteres: 119
        Número total de linhas: 3
        Palavra mais longa: "dificuldade"
    """
    
    write_text = open(read_file_path + "estatisticas.txt", "w")
    write_text.write(f"""Total de palavras: {len(palavras)}
Total de caracteres: {len(caracteres)}
Numero total de linhas: {linhas}
Palavra mais longa: {longWord}""")
    
    write_text.close()
  
except Exception as error:
    print(f"Error detected{error}")
    
finally:
    print("Obrigaod por usar o programa :)")