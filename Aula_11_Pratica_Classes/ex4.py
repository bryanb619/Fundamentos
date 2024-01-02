# classe character 

damage = 10

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

    #-----------------------------------------------------------
class Warrior(Character):
    
    def __init__(self, name, health, strength, defense):
        super().__init__(name, health, strength, defense)
    
    def berserk(self, target):
        target.health -=  damage * 4
        print(f"{self.name} goes beserk! and attacks {target.name} causing {damage} damage. {target.name} has {target.health} health")
    
    #-----------------------------------------------------------
class Mage(Character):
    def __init__(self, name, health, strength, defense):
        super().__init__(name, health, strength, defense)

    def cast_spell(self, target):
        target.health -=  damage * 3
        print(f"{self.name} casts a spell on {target.name} causing {damage} damage. {target.name} has {target.health} health")
        
    def attack(self, target):
        newDamage = damage * 3
        target.health -=  newDamage
        
        print(f"{self.name} attacks {target.name} causing {newDamage} damage")
        
    #-----------------------------------------------------------
    
class Archer(Character):   
    def __init__(self, name, health, strength, defense):
        super().__init__(name, health, strength, defense)
         
    def shoot_arrow(self, target):
       
        target.health -=  damage * 2
        print(f"{self.name} shoots an arrow at {target.name} causing {damage} damage. {target.name} has {target.health} health")
   
   #-----------------------------------------------------------
   
   
   
warrior = Warrior("Thorin", 120, 25, 15)
mage = Mage("Gandalf", 80, 10, 5)
archer = Archer("Legolas", 90, 20, 10)
enemy = Character("Enemy", 50, 15, 5)

mage.attack(enemy)

archer.attack(warrior)