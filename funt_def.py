# print is function in python
# function is a block of code which only runs when it is called
# you can pass data, known as parameters, into a function
# a function can return data as a result


# here i would like for us to define a function 

def print_out(s):
    print(s)
    print(s + "hello this is my simple definition")

print(print_out("what is this? "))

print_out("what is this? ")

def times_two(x):
    return x*2

r = 5
print(times_two(r))
print(r) # r is not changed because we did not change it in the function, we just returned a new value

# you can add return 

def append_list(m):
    m.append(4)
   

a =[1 , 2 , 3]
append_list(a)
print(a) # a is changed because we passed the list to the function and we modified it in the function, we did not return a new value, we modified the original list
 