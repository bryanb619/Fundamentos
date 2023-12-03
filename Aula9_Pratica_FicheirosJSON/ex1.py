filepath = "D:\Projects\Exercises\FP\Aula9_Pratica_FicheirosJSON"

myInput = input("type the filename without extension: ")


myInput = myInput.lower()
myInput = filepath + "/" + myInput + ".txt"

file = open( myInput, "rt")

all_lines = file.readlines()


for line in all_lines:
    print(line)

file.close()