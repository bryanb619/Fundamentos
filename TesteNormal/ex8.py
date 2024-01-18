""" [2v] Crie um programa que receba uma string no formato dia/mês/ano, separado por barras; 
parta a data nos seus componentes(verificando se foram dados um número válido de componentes) e valide, 
confirmando se é uma data válida (se o mês dado tem o número de dias apropriado). 
Pode usar a função is_leap_year criada na alínea anterior.
"""


"OBS: Não sei se é a melhor forma"

""" Validação de mês

    1. separar a data em dia, mês e ano (usando o método split)
    -   1.1 dia = date[0] -> posição 0 da lista date (dia)
    -   1.2 month = date[1] -> posição 1 da lista date (mês)
    
    2. Verificar se o número de elementos da lista é diferente de 3
    
    3. verificar se o mês é válido (está contido no dicionário months) 
    4. verificar se o dia é válido (se o dia é menor ou igual ao número de dias do mês dado)
    5. Caso contrário, o dia não é válido (retornamos a posição 1 de date, que é o mês e a 
    mesma posição do dicionário months para obter o número de dias do mês dado)
    
    6. O mês inserido não é válido, porque está fora do dicionário months
    
"""
def is_month_valid(u_date):
    
    # 1.
    date = u_date.split("/")
    
    # 1.1
    day = date[0]
    # 1.2
    month = date[1]
    
    # 2.
    if len(date) != 3:
        return "A data tem de ter o formato dd/mm/yy!"
    
    # 3.
    elif month in months:
        
        # 4.
        if int(day) <= months[date[1]]:
            return "A data é válida!"
        
        # 5.
        else:
            return f"O mês {date[1]} só tem {months[date[1]]} dias!"
        
    # 6.
    else:
        return f"O mês {date[1]} não é válido!"



months = {
    "1":31, 
    "2":28, 
    "3":31, 
    "4":30, 
    "5":31, 
    "6":30, 
    "7":31, 
    "8":31, 
    "9":30, 
    "10":31, 
    "11":30, 
    "12":31
}


print(is_month_valid("1/2")) # A data tem de ter o formato dd/mm/yy!

print(is_month_valid("32/1/2022")) # O mês 1 só tem 31 dias!

print(is_month_valid("29/1/2022")) # A data é válida!

print(is_month_valid("3/9/2022")) # A data é válida!

print(is_month_valid("3/24/2022")) # O mês 24 não é válido!