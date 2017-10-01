#Program to enter comma separated number from console and convert into List and Tuples

values=input("Enter numbers in comma separated format :")
l=values.split(",")
t=tuple(l)
print(l)
print(t)