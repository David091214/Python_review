

p = 'sample.txt'

with open(p, 'r') as f:
   # print(f.readlines( ))
   for item in f:
        #print(item) # this will print each line in the file as a string, including the newline character at the end of each line
        print(item.rstrip()) # this will print each line in the file as a string, including the newline character at the end of each line
    #print(f.read()) # this will read the whole file as a string and print it out