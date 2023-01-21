sub1 = int(input("Enter first subject marks:  "))
sub2 = int(input("Enter second subject marks:  "))
sub3 = int(input("Enter third subject marks:  "))

if (sub1 < 33 or sub2 < 33 or sub3 < 33):
    print("You are fail becouse you have less than 33 percentage in one of the subjects ")
elif ((sub1+sub2+sub3)/3) < 40:
    print("you are fail due to total percentage less then 40")
else:
    print("You are pass.")
