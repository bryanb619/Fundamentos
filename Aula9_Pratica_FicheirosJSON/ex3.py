

def receive_array(lines):

    my_dict = {}

    for line in lines:

        words = lines.split()

        for word in line:

            word = word.strip(".,;'-").lower()
            if len(word) >= 7:
                if word in my_dict:
                    pass
                else:
                    my_dict[word] = len(word)

    print(my_dict)




file = open("text" + ".txt", "rt")

all_lines = file.readlines()

file.close()

receive_array(all_lines)





    

