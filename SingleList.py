# class single_list():

#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next

#     def __str__(self):
#         return str(self.val)
    
# Head = single_list(5)
# A = single_list(3)
# B = single_list(2)
    

# Head.next =A
# A.next = B

# print (Head)

# # traversing the list   

# curr = Head

# while curr:
#     print(curr.val)
#     curr = curr.next
    
# def display(Head):
#     curr = Head
#     element = []
#     while curr:
#         element.append(str(curr.val))
#         curr = curr.next
#     print(' -> '.join(element))
     
# display(Head)



class node:
    def __init__(self, val=None, next = None):
        self.val = val 
        self.next = next 

class LinkedList:
        def __init__(self):
             self.head = node()

        def add(self,val):
            new_node = node(val)
            curr = self.head
            while curr.next!= None:
                curr = curr.next
            curr.next = new_node

        def length(self):
            curr = self.head
            length = 0
            while curr.next != None:
                length += 1
                curr = curr.next 
            return length
        
        def display(self):
            element =[]
            curr_n = self.head
            
            while curr_n.next != None:
                
                curr_n = curr_n.next 
                element.append(str(curr_n.val))
            print('->'.join(element))

        def get(self, value):
            curr = self.head
            if curr.next == None:
                print("no value in the list")
            else:
                curr = curr.next
                count = 0 
                while curr != None:
                    if curr.val ==value:
                        print(f"value {value } is at index {count}")
                        return count 
                    else:
                        curr = curr.next 
                        count +=1

        def erase(self,index):
                curr = self.head
                if curr.next == None:
                    print ("no value in the list")
                else:
                    curr = curr.next
                    prev = self.head
                    count = 0
                    while curr != None:
                        if index >= self.length():
                            print("index out of range, try something smaller")
                            return
                        else:
                            while count != index:
                                prev = curr
                                curr=curr.next
                                count +=1
                            else:
                                print(f"value {curr.val} at index {index} is deleted")
                                prev.next = curr.next
                                curr = None
                              
                                return

            # curr = self.head
            # count = 0

            # while curr != None:
                                    
            #     if curr.val == value:
            #       print(f"value {value} is at index {count}")
            #       return count
            #     else:
            #      curr = curr.next
            #      count += 1
            # print("value not in the list")  

        def get_value_at_index(self, index):
            curr = self.head
            if  curr is None:
                print("no value in the list")
            else:
                curr = curr.next
                if index >= self.length():
                    print("index out of range, try something smaller")
                else :
                    count =0
                    while curr != None:
                        if count == index:
                            print(f"value at index {index} is {curr.val}")
                            return curr.val
                        else:
                            curr = curr.next
                            count += 1
                

                
                         



myL = LinkedList() # this is the head of the linked list]


myL.add(5)
myL.add(3)
myL.add(2)

myL.display()
myL.get(2)
myL.get_value_at_index(2)

myL.erase(3)
myL.display()
             

# a = node(5)
# print(a)    
