# unwanted characters
unwanted_chars = ['.', ',', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{', '}', '"', "'"]


def string_processor(my_string):

    # convert all characters to lowercase
    my_string = my_string.lower()
    # remove start end end whitespace
    my_string = my_string.strip()

    # replace each unwanted character with an empty string (NO SPACE)
    for char in unwanted_chars:
        my_string = my_string.replace(char, '')

    # Turn the string into a list of words
    my_string = my_string.split()

    # call the string_repetition function sending our processed string as a parameter
    string_repetition(my_string)


# accept a list of strings as a parameter
def string_repetition(string_list):
    # create our empty dictionary
    string_dict = {}

    # loop through each word in the list and add it to the dictionary
    for word in string_list:
        if word in string_dict:
            # if the word(word is our key) is already in the dictionary, increment the value by 1( is our value)
            string_dict[word] += 1
        else:
            string_dict[word] = 1

    # print the dictionary
    print(string_dict)





