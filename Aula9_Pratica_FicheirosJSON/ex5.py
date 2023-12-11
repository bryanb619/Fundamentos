import json

""" 1. Path to the file
    2. open file i read mode
    3. read the file we use {json_ data} 
        that will be our data to be read from the file
    4. data variable will be a dictionary that receives the info
        json.loads(_json_data_) pushes info to the data variable (our new dictionary)
    5. print data

"""
# 1.
json_path = "D:\\Projects\Exercises\FP\Aula9_Pratica_FicheirosJSON/text_data.json"
 
# 2.
file = open(json_path, "r")

# 3.
json_data = file.read()

# 4.
data = json.loads(json_data)

# 5.
print(data)

# 6.
file.close()