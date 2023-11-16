from collections import deque

players_list = ['Jack', 'Alice', 'Bob', 'Joane']

fila = deque()

fila.extend(players_list)


# temos de fazer append right para adicionar o player ao fim da fila ao fim do turno
def add_player_end_quue(player):
    fila.popleft()
    fila.append(player)
    print(fila)


add_player_end_quue(fila[0])



