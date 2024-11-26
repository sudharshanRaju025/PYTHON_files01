str=input("enter the string name:")
print(str)
print(len(str))
revstr=""
def revstring(a):
    for i in str:
        global revstr
        revstr=i + revstr
    return revstr
    
print(revstring(str))