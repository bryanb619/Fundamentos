# points variable
points = 0

def receive_point(funçãoLambda):
    # declarar variável global
    global points
    # igual a chamar uma função, neste caso uma função lambda
    points = funçãoLambda(points)
    # retornar o valor de points
    return points
   
# imprimir points
print(f"You've received {receive_point(lambda x: x + 300)} points")



