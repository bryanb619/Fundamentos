# classe character 

damage = 15

CHARACTERS = []

class Character:
    
    # attributes
    name        = ""
    health      = 0
    strength    = 0
    defense     = 0
    
    # constructor
    def __init__(self, name, health, strength, defense):
        self.name       = name
        self.health     = health
        self.strength   = strength
        self.defense    = defense
        
        CHARACTERS.append(self)
        
    def attack(self, target):
        
        target.health -=  damage
        
        print(f"{self.name} attacks {target.name} causing {damage} damage")
    
    def defend(self, target):
        target.health = target.health - 35
        print(f"{self.name} defends himself from {target.name}. Enemy has {target.health} health!")
   
       
hero = Character("Hero", 100, 20, 10)
enemy = Character("Enemy", 100, 20, 10)

hero.attack(enemy)
enemy.defend(hero)
