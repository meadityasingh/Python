# d = {110:"abc", 101:"xyz", 105:"pqr"}
# print(d)

# d = {}                      #empty dictionary
# print(d)

# d["laptop"] = 40000
# d["mobile"] = 50000
# d["earphone"] = 1000
# print(d)
# print(d["mobile"])


#get function 
d = {110:"abc", 101:"xyz", 105:"pqr"}
print(d.get(101))     #when you provide key to get function it will give you a value coresponding to get function 
print(d.get(125))     #if  key doese not exist in the dictory it give output as none , it will not through an error


print(d.get(125, "NA"))
       #OR
if 125 in d:
    print(d[125])
else:
    print("NA")

d[101] = "wxy"
print(len(d))
print(d)

print(d.pop(105))
print(d)

del d[110]
print(d)

d[108] = "cde"
print(d)
print(d.popitem())  #remove last added item 
print(d)
