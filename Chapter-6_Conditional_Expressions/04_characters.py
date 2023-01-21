# Print 10 characters present in a Username
username = input("Username is ")

if (len(username)) < 10:
    print("less then 10 charecter in username.")
elif (len(username)) == 10:
    print("10 charecter in username.")
else:
    print("greater then 10 charecter in username.")
