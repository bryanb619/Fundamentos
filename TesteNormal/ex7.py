""" 7. [1v] Crie uma função is_leap_year que retorne true se o ano dado é bisexto. 
Um ano é bisexto se é divisível por 4, a não ser anos fim de século (1800, 1900, 2000) que são também divísiveis por 400.
"""

""" Ano bissexto

    1. Se o ano for divisível por 4 e não for divisível por 100, é bissexto
    
    2. Se o ano for divisível por 400, é bissexto
    
    3. Caso contrário, não é bissexto
"""
def is_leap_year(year):
    
    # 1.
    if year % 4 == 0 and year % 100 != 0:
        return True
    
    # 2.
    elif year % 400 == 0:
        return True
    
    # 3.
    else:
        return False
    
    
print(is_leap_year(1900)) # False

print(is_leap_year(2000)) # True

print(is_leap_year(1996)) # True

print(is_leap_year(2002)) # False


