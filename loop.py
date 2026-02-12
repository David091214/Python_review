 # a simple variable to hold list of items 
My_List = ["apple", "orange", "fish"]
print(My_List)

 # append to the list of items 
My_List.append("fruits")


# for loop 
# using item as an iterate varianle

for item in My_List:
    print(item)

    #indexing is [i]

    # and index is i

    #example

for i in [0,1,2,3]:
    print(My_List[i])

    # or

for i in range(4): # n -1 = 3 so it is same as 0 ,1 , 2,3
    print(My_List[i])

# we can also conver range(4) to a list 
list(range(4))
list(range(len(My_List)))

for i, item in enumerate(My_List):
    print(i, item)