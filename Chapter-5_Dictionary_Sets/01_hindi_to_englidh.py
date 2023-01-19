myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "vastu": "Item"
}
print("Opction are", myDict.keys())
a = input("Enter Hindi Word\n")
# print("The meaning of your word is:", myDict[a])
# Below line will not an error if the key is not preasent in dictionry
print("The meaning of your word is:", myDict.get(a))
