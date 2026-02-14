A = [1 , 2,3, 4] # O(1)
print(A)


A.append(6) # O(1)
print(A)

A.pop(2) # O(1)
print(A)

A.insert(2 , 3) # O(n)
print(A)


print(A[0])

if 6 in A: 
    for i in A:
        if i == 6:
            print(f" found 6 at index {A.index(6)} ")
else:
    print("not found" ) 

print(len(A)) # O(1)