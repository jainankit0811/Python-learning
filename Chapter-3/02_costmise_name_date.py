Letter = '''Dear <|name|>,
You are selected!

Date: <|Date|>
'''
name = input("Enter your Name\n")
date = input("Enter Date\n")

Letter = Letter.replace("<|name|>", name)
Letter = Letter.replace("<|Date|>", date)

print(Letter)
