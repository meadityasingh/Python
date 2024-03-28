# s1 = {10, 20, 30}
# print(s1)

# s2 = set([20, 30, 40])      #create a set out of list
# print(s2)

# s3 = {}                     #this will create an empty disctionary
# print(type(s3))

# s4 = set()                  #this will  create empty set
# print(type(s4))
# print(s4)

# #insetion in set 
# s = {10, 20}
# s.add(30)
# print(s)
# s.add(30)                   #here it will not add 30 as this value already present in the set, and set will not have duplicate value
# print(s)
# s.update([40,50])
# print(s)
# s.update({60, 70}, [80, 90])
# print(s)

# #removal operation on set
# s = {10, 30, 20, 40}
# print(s)
# s.discard(30)                 #delete 30, if item is not present in set it will not perform any action
# print(s)
# s.remove(20)                  #raise an error if the item is not in set
# print(s)
# s.clear()                     #everything will remove from collections you will have empty set
# print(s)
# s.add(50)
# print(s)
# del s                        #it will delte the object of set 
# #print(s)

# s = {10, 20, 30}
# print (len(s))
# print (20 in s)
# print(50 in s)


###############################################################################################

# s1 = {2, 4, 6, 8}
# s2 = {3, 6, 9}

# print(s1 | s2)              #union of two set
# setun = s1.union(s2)
# print(setun)

# print (s1 & s2)           #intersection of two set 
# setin = s1.intersection(s2)
# print(setin)

# print (s1 - s2)
# setdiff = s1.difference(s2)
# print(setdiff)

# print (s1 ^ s2)          #symmitric difference element present in both the set but not common
# setsym = s1.symmetric_difference(s2)
# print ( setsym)

###############################################################################################
s1 = {2, 4, 6, 8}
s2 = {4, 8}

print(s1.isdisjoint(s2))         #boolean value -> true if no common element in set --> false if there is a common element 

print(s1 <= s2)                  #issubset operator s1 is subset of s2 or not 
print(s1.issubset(s2))

print(s1 < s2)                   #if s1 is proper set of s2 or not    IF true the s1 should have less element and all the elementof s1 should present in s2

print(s1 >= s2)                   #if s1 is superset  of s2 or not    IF true the s1 should have all the  element present in s2
print(s1.issuperset(s2))

print(s1>s2)                   #propersuperset
