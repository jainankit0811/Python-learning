text = input("Enter comment: ")

if ("make a lot mony" in text):
    spam = True
elif ("buy now" in text):
    spam = True
elif ("click this " in text):
    spam = True
elif ("subcribe this" in text):
    spam = True
else:
    spam = False

if (spam):
    print("This text is spam")
else:
    print("This text is not spam")
