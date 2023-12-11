import random

characterList = []
Item = [("Skeleton's Gut", 5), Gem("Diamond"), Gear("Helm", 10)]

class Faction:
    Player = 0
    Enemy = 1
    Npc = 2
    # --------------------------------------
    

class CharacterClass:
    name = ""
    hp_base = 0
    hp_random = 0
    gold = 0
    
    
    def __init__(self, class_name, hp_base, hp_random_max, gold):
        self.name = class_name
        self.hp_base = hp_base
        self.hp_random = random.randint(0,hp_random_max) 
        self.gold = gold
        # --------------------------------------
        
        
class Character:
    name=""
    class_name = None
    hp = 0
    gold = 0
    
    inventory = []
    
    def __init__(self, CharClass, hp, gold):
        
        self.class_name = CharClass
        self.hp = hp
        self.gold = gold
        
    def take_action(self):
        print(f"{self.name} does nothing...")
        # --------------------------------------
        
        
    
class Player(Character):
    
    def take_action(self):
        
        print("""1 - Sell
            2 - Loot
            3 - Attack \n""")
        
        action = input("What do you want to do?")  
        
        if action == "1":
            self.sell_item()
            
        elif action == "2":
            self.loot_item()
            
        elif action == "3":
            self.attack()
            
        else:
            print("Invalid input!")
           
    # Sell item 
    def sell_item(self):
        print("You can't sell items!")
        
    # Loot item
    def loot_item(self):
        print("You can't loot items!")
    
    # Attack
    def attack(self):
        print("You attack!")
        
        
    
        
class Enemy(Character):
    
    def take_action(self):
        
        action = random.choice(["attack","wait"])
        
        if action == "attack":
            print(f"{self.name} attacks!")
            
        elif action == "wait":
            print(f"{self.name} waits!")
    # --------------------------------------
 
            
class NPC (Character):
    def take_action(self):
        return super().take_action()
    # --------------------------------------
        
    
    
class Item():
    name = ""
    value = 0
    
    def can_equip(self):
        return False
        
    
class Gear(Item):
    
    def can_equip(self):
        return True
    
    
class Gem(Item):
    
    def __init__(self, name):
        value = random.randint(100,201)
        super().__init__(name, value)
    
    
        
            
        
        

    
    
        
