# programa que arruma uma lista de tuplos usando lambda


def arrange_array(some_list, function):
    
    n = len(some_list)
    
    for i in range (n):
        
        for j in range (n -i -1):
            
            if not function(some_list[j][1], some_list[j+1][1]):
                # trocas posições
                some_list[j], some_list[j+1] = some_list[j+1], some_list[j]
                
    return some_list
            


my_set = [('English', 88),
          ('Science', 90),
          ('Maths', 97),
          ('Social sciences', 82)]


arrange_array(my_set, lambda a,b : a<b)

print(my_set)
