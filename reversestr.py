str=input("enter the string:")
print(str)
def string(str):
    name=""
    for j in str:
        name=j + name
    return name

print(string(str))