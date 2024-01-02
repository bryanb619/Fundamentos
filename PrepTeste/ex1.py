
def countDown(n):
    
    if n == 0:
        return "Liftoff!"
    
    return f"\n {n} {countDown(n-1)}"


print(countDown(5))


 #return str(n) + "\n" + countDown(n -1) 



