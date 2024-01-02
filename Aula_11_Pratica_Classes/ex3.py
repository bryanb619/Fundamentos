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
    def __init__(self, name, health, strength, defense, inventory = []):
        self.name       = name
        self.health     = health
        self.strength   = strength
        self.defense    = defense
        self.inventory  = []
        
        CHARACTERS.append(self)
        
    def attack(self, target):
        
        target.health -=  damage
        
        print(f"{self.name} attacks {target.name} causing {damage} damage")
    
    def defend(self, target):
        target.health = target.health - 35
        print(f"{self.name} defends himself from {target.name}. Enemy has {target.health} health!")
   
    def equip(self, gear):
        self.inventory.append(gear)

        if gear.name == "Sword":
            self.strength += gear.damage
            print(f"{self.name}'s strength is now {self.strength}")
            
        elif gear.name == "Helm":
            self.defense += gear.defense
            print(f"{self.name}'s defense is now {self.defense}")
            
        else:
            print("You can't equip that!")
     
    
    
class item():
    def __init__(self, name):
        self.name   = name
    

class weapon(item):
    
    def __init__(self, name, damage):
        super().__init__(name)
        self.damage = damage


class armor(item):
    def __init__(self, name, defense):
        super().__init__(name)
        self.defense = defense
        
        
       
hero = Character("Hero", 100, 20, 10)
enemy = Character("Enemy", 100, 20, 10)

hero.attack(enemy)
enemy.defend(hero)

sword = weapon("Sword", 5)
helm = armor("Helm", 3)


hero.equip(sword)
hero.equip(helm)
