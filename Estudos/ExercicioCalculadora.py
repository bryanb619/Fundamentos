import json

# Path onde o ficheiro log.json está guardado
path = "Estudos/"

# Variável global que conta quantas vezes o programa foi executado
timesRun = 0

""" calculate
    Função que realiza as operações matemáticas básicas
    e retorna o resultado da operação.
    
    params:
        op: operação matemática
        num1: primeiro número
        num2: segundo número
"""
def calculate(op, num1, num2):
    
    global timesRun
    timesRun += 1
        
    if op == "+":
        return f"{num1} + {num2} = {num1 + num2}"
    
    elif op == "-":
        return f"{num1} - {num2} = {num1 - num2}"
    
    elif op == "*":
        return f"{num1} * {num2} = {num1 * num2}"
    
    elif op == "/":
        return f"{num1} / {num2} = {num1 / num2}"
    
    elif op == "%":
        return f"{num1} % {num2} = {num1 % num2}"
    
    elif op == "//":
        return f"{num1} // {num2} = {num1 // num2}"

    else:
        return f"Operador {op} inválido!"
        
        
""" save_log 

    1. Abre o ficheiro log.json lendo seu conteúdo.
    2. Guarda o resultado da operação num ficheiro json.
"""
def save_log(dict):
    
    print("Salvando log...")
        
    read_file = open(path + "log.json", "r")
    file_content = json.load(read_file)
    # file content
    file_content.append(dict)
    read_file.close()
    
    write_file = open(path + "log.json", "w")
    json.dump(file_content, write_file, indent=4)
    print("Log salvo com sucesso!")
    write_file.close()
    
    
def display_log(display_history = False):
    
    read_file = open(path + "log.json", "r")
    file_content = json.load(read_file)
    lastData = file_content[-1]
    read_file.close()
    
    
    if display_history == True:
        file_content_reversed = file_content[::-1]
        for line in file_content_reversed:
            print(line)
    else:
        print(lastData)
    
        
""" main

    com while True:
        pedir input ao utilizador
 
"""
def main():
    
    while True:
        
        try:
            display_log()
            
            op = input("\nQual a operação que deseja realizar? (+, -, *, /, %, **, //, sair, ler): ")

            if op == "sair":
                break
            
            if op == "ler":
                display_log(True)
                op = input("\nQual a operação que deseja realizar? (+, -, *, /, %, **, //, sair, ler): ")
                

            
            num1 = float(input("Insira o primeiro número: "))
            num2 = float(input("Insira o segundo número: "))

                
            displayCalc = calculate(op, num1, num2)

            my_dict = {"result": displayCalc}
            
            save_log(my_dict)
            
            
            print(displayCalc)
            
            print(f"O programa já foi executado {timesRun} vez(es)\n")

            
        except Exception as e:
           print("Erro: ", e)
           
        finally:
            print("Fim do programa!")
    

main()