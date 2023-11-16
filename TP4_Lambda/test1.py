my_string = "This is a sentence and I want to count the characters in it!"
my_dict = {}


def conta_letras(words):
    for i in words:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    print(my_dict)


conta_letras(my_string)