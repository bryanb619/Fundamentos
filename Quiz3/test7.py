def my_fileExist():
    
    try:
        file = open('dados.txt', 'r')
        
        all_lines = file.readlines()
        
        file.close()
        return True
        
    except FileNotFoundError:
        return False
        

if my_fileExist():
    print("File exist")
    
else:
    print("File not exist")