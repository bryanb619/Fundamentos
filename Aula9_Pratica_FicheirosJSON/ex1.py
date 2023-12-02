myInput = input("type the filename without extension: ")


file = open(myInput + ".txt", "rt")

all_lines = file.readlines()


for line in all_lines:
    print(line)

file.close()