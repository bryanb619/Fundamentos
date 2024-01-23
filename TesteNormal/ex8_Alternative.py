def is_leap_year(y):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
               

def get_max_days(m,y):
    if m == 2:
        if is_leap_year(y):
            return 29
        else:
            return 28
    if m in [ 1, 3, 5, 7, 8, 10, 12 ]:
        return 31
    else:
        return 30

def check_date(date_string):
    s = date_string.strip().split('/')
    if len(s) != 3:
        print("A data tem de ter formato dd/mm/yyyy")
        return False
    try:
        day = int(s[0])
        month = int(s[1])
        year = int(s[2])
    except:
        print("O formato tem de ser numérico (dd/mm/yyyy)")
        return False
   
    if (month < 1) or (month > 12):
        print("O mês tem de estar compreendido entre 1 e 12")
        return False
   
    max_days = get_max_days(month, year)
    if (day < 1) or (day > max_days):
        print(f"O mês {month} só tem {max_days} dias!")
        return False

    print("A data é válida!")

    return True

while (True):
    d = input(">")
    check_date(d)