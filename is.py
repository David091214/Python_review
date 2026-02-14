# is remembers memeory not the exact value 
# example

a = [1, 2, 3]
b = a
a.append(4)
print (a) # this is [1, 2, 3, 4] because we modified the original list that a and b are pointing to
print (b) # this is also [1, 2, 3, 4
  
print (a is [1, 2, 3]) # this is false because a and [1, 2, 3] are not the same object in memory
print (a is b) # this is true because a and b are the same object in

#different asnwers

from copy import deepcopy

b = deepcopy(a) # this creates a new object in memory that is a copy of a
print ("\n" , a is b) # this is false because a and b are not the same object

a[0] = 9

print (a)
print (b)


print (a is b) # this is still false because a and b are not the same object in memory