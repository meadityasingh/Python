# t = (10, 20, "geek")
# print(t)
# t = ()                  #this will create empty tuple
# print(type(t))
# print(t)
# t = (10)                #it will not create a tuple with single item 
# print(type(t))
# t = (10,)
# print(type(t))


t = 10, 20, 30, 40, 10
print(t[2])
print(t[-1])
print(t[1:3])            #this will print from index 1 to 2, last index3 element will not be prented
print(len(t))
print(t.count(10))       #count number of time we will get 10
print(t.index(20))