s=int(input("Entet the number of key:value pairs to be added:"))
d={}
for i in range(s):
    key=input("Enter the key(int) to be added:")
    value=[]
    for i in key:
        if i in "aeiouAEIOU":
            value.append(i)
    d.update({key:value})
print("Updated dictionary is:")
print(d)    







