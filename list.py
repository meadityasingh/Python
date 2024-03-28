#List
l = [10, 20, 30, 40, 50]
print(l)                    #print list
print(l[3])                 #print item at index 3
print(l[-1])                #print last item
print(l[-2])                #print second last item
l.append(30)                #append item 30 at end of list
print(l)                    
l.insert(1, 15)             #15 is going to instered at index 1 and item from index 1 going to shift to right side
print(l)
print (15 in l)             #in operator to check item present in the collection
print (l.count(30))         # count the occurance of an item in collection
print (l.index(30))         #index function tell the first occurance of item.
print (l.index(30,4,7))     #index search between 4 to 7
l.remove(20)                #remove value 
print(l)
print(l.pop())              #remove the last value and reture the removed value
print(l)
print(l.pop(2))             #remove item at index 2 and return the value at index 2
print (l)
del l[1]                    #remove item at index 1
print (l)
del l[0:2]                  #remove item at index 0 and 1
print (l)
#l = [10, 40, 20, 50]
l = ["aditya", "anived", "abhishek"]

print (l)
print (max(l))
print (min(l))
#print (sum(l))
l.reverse()
print(l)
l.sort()                    #sort the listin creasing order 
print(l)