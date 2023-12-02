dataFile = "D:\Projects\Exercises\FP\ExerciciosDiogo\Ficheiros\data.txt"

# unwanted chars
unwanted_chars = [".", ",", "!", "?"]

# empty dictionary 
userNameData = {}



"""  Open the file 'dataFile' file in (r)ead mode
    1. Read all lines
    2. For loop to read all lines and apply the operations below (3 - 5)
    3. For loop to replace all 'unwanted_chars' in the text
    4. strip() and split() all lines turns into a list 
    5 loop through the list and add to the dictionary 'userNameData'
        - newDataType[0] is the key for the dictionary user name
        - newDataType[1] is the value for the dictionary user age
        - #newDataType[2] is the value for the dictionary user city
        - | is a delimiter to split the data further
        
    6. Close the file {dataFile}
"""

def open_data_file():
    file = open(dataFile, "r")

    allLines = file.readlines()

    # 2.
    for line in allLines:

        # 3.
        for char in unwanted_chars:
            line = line.replace(char, "")

        # 4.
        newDataType = line.strip().split()
        
        # 5.
        for user in newDataType:
            userNameData[newDataType[0]] = {"Dados":f"Idade= {newDataType[1]}|Cidade= {newDataType[2]}"}
            
        # 6.
        file.close()


""" Main Program

    While loop 

    1. Ask the user to input a name
    2. Capitalize the input 
        2.1. If the input type "Sair" break the loop
    
    3. Try Block
    4. Except Block
    5. Finally Block
"""
def Program_loop():
    
    while True:
        
        # 1.
        inputUser = input("Inserir nome de utilizador: ")
        
        # 2.
        inputUser = inputUser.capitalize()
        
        # 2.1.
        if inputUser == "Sair":
            print("A sair...")
            break
        
        """  Try block
            3.1 Check if the inputUser is in the dictionary {userNameData}
            3.2. Use Split() to split the info at | as delimiter 
            3.3. Print the info
            
            3.4 If the inputUser is not in the dictionary print "Pessoa não existe!"
        """
        try:
            
            # 3.1.
            if inputUser in userNameData:
                
                # 3.2 split age and city at white space
                age, city = userNameData[inputUser]['Dados'].split("|")

                # 3.3
                print(f"Qual o nome> {inputUser}")
                print(age)
                print(city)
                
                
            # 3.4
            elif inputUser not in userNameData:
                print(f"Pessoa não existe {input}!")
                
        # 4. 
        except:
            print("Erro desconhecido!")
            
        # 5.
        finally:
            print("A recomeçar...")
    
    

open_data_file()
Program_loop()




# Test data types
#print(f"{users}")
#print(userNameData)
#print(userNameData["Maria"])
#userNameData["userName"] = {"Data":21}
#userNameData["Steven"] = {"Data":23}





    