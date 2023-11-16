my_name = "Legolas"
my_class = "Rogue"
level = 1


game_state = {"Name" : my_name,
              "Class": my_class,
              "Level": level,}


# 01
print (game_state)

# 02 print level 
print (game_state["Level"])

# 03
game_state["Level"] = 22
print (game_state["Level"])

#04
game_state["Bow"] ="Wooden Bow"
game_state["Potion"] = "Healing Potion"
print (game_state) 

# 05
del game_state["Potion"]
print (game_state)


# 06
if "characterMap" in game_state:
    print (game_state["characterMap"])

else:
    game_state["characterMap"] = (1,2)
    print (game_state["characterMap"])


# 07
"""
for myDictId in game_state:
    print (myDictId, game_state[myDictId])
    
"""

for key, value in game_state.items():
    print ("Key:", key, "| Value:", value)

    



