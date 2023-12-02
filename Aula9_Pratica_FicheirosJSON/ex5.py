import json

file_name = "text_data"

file = open(file_name +".json", "rt")

data = json.load(file)

print(f"This is JSON file{data}")

file.close()
