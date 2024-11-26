def name(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("enter the string:")
print(name(s))
