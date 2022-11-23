sagar=input("enter a string :")

length=len(sagar)
if length>2:
    if sagar[-3:]=="ing":
        sagar +="ly"
    else:
        sagar +="ing"
print(sagar)
