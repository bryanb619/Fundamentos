import string
import random

specialChars = ["!", "@", "#", "$", "%", "&", "*"]
randomize = ""

def gera_password(lenPass, caps = False, lowerCase = False, HasNumbers = False, HasSpecialChars = False):
    
    global randomize
    
    
    if lenPass <= 0:
        return "Password length must be greater than 0"
    
    while len(randomize) < lenPass:

        """Caps """
        if caps == True:
            randomize += random.choice(string.ascii_uppercase)

        """LowerCase """     
        if lowerCase == True:
            randomize += random.choice(string.ascii_lowercase)
            
        """Numbers"""
        if HasNumbers == True:
            randomize += random.choice(string.digits)
            
        """SpecialChars"""
        if HasSpecialChars == True:         
            randomize += random.choice(specialChars)
            
    return randomize
                
                
password = gera_password(5, True, True, False, True)
# Podia devolver aB%6kJ!
print(password)