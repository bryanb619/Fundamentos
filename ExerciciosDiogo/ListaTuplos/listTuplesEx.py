stock = [("Camisa", 50, 29.99), ("Calça", 30, 49.99), ("Tênis", 20, 99.99)]

# add camisa
stock.append(("Camisa", 10, 29.99))

# add boné
stock.append(("Boné", 15, 14.99))

#print(stock)


# calcular valor total do stock
def calcular_valor():
    # incializar variável total a 0
    total = 0.0
    for item in stock:
        # para cada intem em stock, buscar a segunda posição, ja que queremos apenas o valor e somar ao total!
        total += item[2]  # => igual a dizer total = total + item[2] =>  total é igual a soma de cada valor de cada item 
    # retornar o total
    return total


# valor total do stock é igual a chamada da função calcular_valor()
valor_total_stock = calcular_valor()

# passo adicional(2 casas decimais (não é necessário, mas deixa mais bonito))
round_number = round(valor_total_stock, 2)

# printar o valor total do stock arrendondado
print("Valor total do stock: ", (round_number))







