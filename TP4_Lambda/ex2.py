rpg_text = "In a dark and mysterious dungeon, the adventurer discovered a hidden treasure chest. Inside the chest, they found ancient artifacts of great power."



def filter_words_by_length(string, length):
    my_dict = {}

    words = string.split()

    for word in words:

        word = word.strip(".,!?")

        if len(word) < length:
            my_dict[word] += 1

    return my_dict


print(rpg_text,5)