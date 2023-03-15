mylist = list()
print("Enter 5 element for the list: ")
for i in range(5):
    val = int(input())
    mylist.append(val)

print("Enter an element to be searched: ")
elem = int(input())

postlist = list()
for i in range(5):
    if elem == mylist[i]:
        postlist.append(i)   

if len(postlist) == 0:
    print("\nElement is not found in the list!")
else:
    print("\nElement is found at position:", postlist[0])    
        

