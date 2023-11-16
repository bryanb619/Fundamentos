names = "Frodo; Aragorn, Boromir and Legolas. Gandalf and Gimli"

badwords = [" and",".",";",","]



for i in badwords:
    
    names = names.replace(i,"")

names = names.split(" ")


print(names)




