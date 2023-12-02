my_array = []

myInput = input("type the filename without extension: ")

file = open(myInput + ".txt", "rt")

all_lines = file.readlines()

my_array.extend(all_lines)

file.close()


#print(my_array)

