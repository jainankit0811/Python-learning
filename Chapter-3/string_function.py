Story = '''once upon a time. there was a crrow.'''

# String Functions
print(len(Story))

print(Story.endswith("crrow."))

print(Story.count("O"))

# It function finds a word and return first occurence of that word in the string.
print(Story.capitalize())

print(Story.find("time"))

# It function replace a all Word in a line
print(Story.replace("once", "one"))

# escape sequences
Story = "Ankit is a good.\nHe is\t a very \\good"
print(Story)
