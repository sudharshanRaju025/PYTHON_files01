num=int(input("enter the number:"))
string=str(num)
print(string)
print(len(string))
revnum=str()
def revnumber(a):
    global revnum
    for i in string:
        revnum=i + revnum
    return revnum
print(revnumber(string))