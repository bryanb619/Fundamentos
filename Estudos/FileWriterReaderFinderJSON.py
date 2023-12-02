import json

# unwanted chars
unwanted_chars = [".", ",", "!", "?"]

# empty dictionary 
userNameData = {}

# data file path
dataJSONFile = "D:\Projects\Exercises\FP\Estudos\dataBase.JSON"


""" JSON File Reader 

    1. initialize an empty dictionary
    2. open the file in (r)ead mode
    3. read the file
    4. print the file in console
    5. close the file
    
"""
def JSON_reader():
    
    # 1.
    userDict = {}
    
    # 2.
    file = open(dataJSONFile, "r")
    
    # 3.
    userDict =  json.load(file)
    
    # 4.
    for user in userDict:
        print(f"Utilizador: {user} {userDict[user]}\n")
    
    # 5.
    file.close()
    
    
""" JSON User Finder
    :param userToSearch: user input from the main program loop
    
    1. initialize an empty dictionary
    2. open the file in (r)ead mode
    3. read the file using json.load()
    4. close the file
    5. if the user is in the dictionary print the user
"""
def JSON_user_finder(userToSearch):
    
    # 1.
    userDict = {}
    
    # 2.
    file = open(dataJSONFile, "r")
    
    # 3.
    userDict =  json.load(file)
    
    # 4.
    file.close()
    
    
    # 5.
    if userToSearch in userDict:
        print(f"Utilizador encontrado: =>{userToSearch}{userDict[userToSearch]}\n")
    
    # 6.
    elif userToSearch not in userDict:
        print(f"Utilizador não encontrado: =>{userToSearch}\n")
    
    
    

""" JSON File Writer
    :param inputUser: user input from the main program loop

    1. Receive the input from the user 
    2. Try block
        2.1. Ask the user to input the age
        2.2. Ask the user to input the city
        2.3. For loop to replace all 'unwanted_chars' in the text
        2.4. Capitalize the city name
        2.5. Add the user to the dictionary 'userNameData'
        2.6. Open the file in (r)rite mode
           - 2.6.1. Read the file using json.load() attempt to append info later on
           - 2.6.2. Update the dictionary 'oldDict' with the dictionary 'userNameData
        
        2.7. Write the dictionary 'useDict' to the file
           - 2.7.1 dump info to the file using json.dump()
        2.8. Close the file
        
    3. Except block
    4. Finally block
"""
   # 1.
def JSON_writer(inputUser):
    
    # 2.
    try:
        oldDict = {}
                
        # 2.1.
        inputUserAge = input("Inserir idade: \n")
        # 2.2.
        inputUserCity = input("Inserir cidade: \n")
        # ------------------------------------------------
        
        
        # 2.3.
        for char in unwanted_chars:
            inputUserCity = inputUserCity.replace(char, "")
            # ------------------------------------------------
            
        # 2.4.
        inputUserCity = inputUserCity.capitalize()

        # 2.5.
        userNameData[inputUser] = {"Dados":f"Idade= {inputUserAge}|Cidade= {inputUserCity}"}
        
        
        # 2.6.
        file = open(dataJSONFile, "r")
        # 2.6.1 
        oldDict = json.load(file)
        # 2.6.2
        oldDict.update(userNameData)
    
    
        # 2.7.
        file = open(dataJSONFile, "w")
        # 2.7.1
        json.dump(oldDict, file, indent=4)
        
        # 2.8.
        file.close()
        
        
    
    # 3.
    except:
        print("Erro ao adicionar utilizador")
        
    # 4.
    finally:
        print("Obrigado por usar o programa")


    
    
    
""" Main Program

    While loop 

    1. Ask the user to input a name
    2. Capitalize the input 
        2.1. If the input type "Sair" break the loop
        
    3. Show all users
    4. Search for a user
    5. Add a user
    
    

"""
def Program_loop():
    
    while True:
        
        print(""" Insere o nome de utilizador para adicionar 
              Digite 'Sair' para sair do programa
              Digite 'M' para mostrar todos os utilizadores adicionados 
              Digite 'R' para procurar um utilizador \n """)
        
        # 1.
        inputUser = input("Inserir nome de utilizador para adicionar: ")
        
        # 2.
        inputUser = inputUser.capitalize()
        if inputUser == "Sair":
            break
        
        
        # 3.
        elif inputUser == "M":
            JSON_reader()
            
        elif inputUser == "R":
            userToSearch = input("Inserir nome de utilizador para procurar: ")
            
            userToSearch = userToSearch.capitalize()
            
            JSON_user_finder(userToSearch)
          
        # 5.
        else:
            JSON_writer(inputUser)
           
                
           
Program_loop()