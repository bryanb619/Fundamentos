# set of enemies

enemies = {"Goblin", "Dragon","Orc"}

# 01
print("Enemies: ", enemies)

# 02
enemies.add("Troll")
print("Enemies: ", enemies)

# 03 
enemies.remove("Goblin")
print("Enemies: ", enemies)

# 04

if "Dragon" in enemies:
    print("Dragon exists")
else:
    print("Dragon does not exist")


# 05 
print("Number of enemies: ", len(enemies))

for enemy in enemies:
    print(enemy)




