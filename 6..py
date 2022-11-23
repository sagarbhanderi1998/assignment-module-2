# swap two number with temp variable:

x=int(input("enter a number x :"))
y=int(input("enter a number y :"))

temp=x
x=y
y=temp

print(" after swapping number x:",x)
print(" after swapping number y:",y)


# swap two number without temp variable:

x=int(input("enter a number x :"))
y=int(input("enter a number y :"))

x,y=y,x

print(" after swapping number x:",x)
print(" after swapping number y:",y)
