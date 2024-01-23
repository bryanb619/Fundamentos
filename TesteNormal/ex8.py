""" [2v] Crie um programa que receba uma string no formato dia/mês/ano, separado por barras; 
parta a data nos seus componentes(verificando se foram dados um número válido de componentes) e valide, 
confirmando se é uma data válida (se o mês dado tem o número de dias apropriado). 
Pode usar a função is_leap_year criada na alínea anterior.
"""


"OBS: Não sei se é a melhor forma"


def is_leap_year(year):
    
    
    # 1.
    if year % 4 == 0 and year % 400 != 0 and year % 100 !=0:
        #return f"{year} :{True}"
        return True
    
    # 3.
    else:
        #return f"{year} :{False}"
        return False


""" Validação de mês

    1. separar a data em dia, mês e ano (usando o método split)
    -   1.1 dia = date[0] -> posição 0 da lista date (dia)
    -   1.2 month = date[1] -> posição 1 da lista date (mês)
    -   1.3 year = date[2] -> posição 2 da lista date (ano)
    
    2. Verificar se o número de elementos da lista é diferente de 3
    
    3. verificar se o mês é válido (está contido no dicionário months) 
    
    4. verificar se o dia é válido (se o dia é menor ou maior ao número de dias do mês dado)
    -    4.1.  RETURN MESSAGE: O mês inserido só tem x dias!
    -    4.2.  RETURN MESSAGE: A data é válida!
    
    5. O mês inserido não é válido, porque está fora do dicionário months
    
    params: u_date -> data inserida pelo utilizador
    
"""
def is_month_valid(u_date):
    
    
    # 1.
    date = u_date.split("/")
    
    
    # EXTRA - 1. tentar converter os elementos da lista date para inteiros
    try :
        
        # 1.1
        d = int(date[0])
        # 1.2
        m = int(date[1])
        # 1.3
        y = int(date[2])
 
    # erro caso o utilizador insira uma data com o formato errado
    except:
        return "A data tem de ter o formato dd/mm/yy!"
    
    # 2.
    if len(date) != 3:
        return "A data tem de ter o formato dd/mm/yy!"
    
    
    # EXTRA - 2.1 checar se é ano bissexto
    if is_leap_year(y):
        months[2] = 29
        
        
        
    # 3.
    if m in months:
        
        # 4.
        if d < months[m] or d > months[m]:
            # 4.1
            return f"O mês {m} só tem {months[m]} dias!"
        
        # 4.2
        return "A data é válida!"
    
    # 5.
    else:
        return f"O mês {m} não é válido!"

months = {
    1:31, 
    2:28, 
    3:31, 
    4:30, 
    5:31, 
    6:30, 
    7:31, 
    8:31, 
    9:30, 
    10:31, 
    11:30, 
    12:31
}

print(is_month_valid("1/2")) # A data tem de ter o formato dd/mm/yy!

print(is_month_valid("32/1/2022")) # O mês 1 só tem 31 dias!

print(is_month_valid("29/1/2022")) # A data é válida!

print(is_month_valid("3/9/2022")) # A data é válida!

print(is_month_valid("30/2/1996")) # O mês 2 só tem 29 dias!

print(is_month_valid("29/2/1996"))

#print(is_month_valid("3/24/2022")) # O mês 24 não é válido!

print("""
--------------------------------
 """)