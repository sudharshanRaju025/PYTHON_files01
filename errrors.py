str=input("enter the string :")
name=""
def string(a):
    for i in str:
        global name
        name=i + name
        
    return name
a=string(str)
print("reverse of a string:",a)

