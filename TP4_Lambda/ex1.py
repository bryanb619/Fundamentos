rpg_story = """In a distant galaxy, a group of fearless rebels, 
dedicated to freedom and justice, waged an epic battle against the oppressive Galactic Empire.
 Led by their heroic leader, the rebels sought to liberate the entire galaxy from the tyranny of the empire. 
 Their struggle was not in vain as they united the inhabitants of the galaxy in a common cause. 
 The grip the empire had on the galaxy was 
slipping, and the rebels' determination only grew stronger. 
The fate of the entire galaxy now rested on their shoulders as they prepared 
for the ultimate showdown.
""" # this is a string

# keywords
plot_keywords = {"rebels", "galaxy", "empire"} # this is a set

# unwanted characters
unwanted_chars = ".,'?!"


def conta_palavras(words, keywords):

    # Create an empty dictionary to store the word counts
    word_counts = {}


    # Lower case / Split the string into words (Queremos criar uma lista de de palavras), entao fazemos split
    words = words.lower().split()

    # Iterate over each word in the list
    for word in words:

        word = word.strip(unwanted_chars)

        # If the word is in the keywords set, add it to the dictionary
        if word in keywords:
            # If the word is already in the dictionary, increment its count
            if word in word_counts:
                word_counts[word] += 1
            # Otherwise, add the word to the dictionary with a count of 1
            else:
                word_counts[word] = 1
    
    # Retornamos o valor dado pelo dicionario word_counts
    return word_counts

print(conta_palavras(rpg_story, plot_keywords))
