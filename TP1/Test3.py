myString = "This is a badword"


banned_words = ["badword"]

for word in banned_words:
    myString = myString.replace("badword","****")
    print("Censored chat: ", myString)

