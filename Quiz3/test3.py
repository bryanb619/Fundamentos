def processar_dados(fileName):
    file = open(fileName, 'r')
    all_lines = file.readlines()
    file.close()
    
    dict = {}
    
    
    all_lines = [line.strip(",.'") for line in all_lines]
    
    print(all_lines)
    
    
    
processar_dados('Novosdados.JSON')
    