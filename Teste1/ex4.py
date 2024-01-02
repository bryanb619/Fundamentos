

def countDown(n):
    
    if n == 0:
        return "Liftoff!"

    else:
        return n + countDown(n -1)
    
    
print(countDown(5))
