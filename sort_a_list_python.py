lst = []
print("Enter 3 numbers, one at a time: ")
for i in range (3):
    lst.append(eval(input()))
    lst.sort()
    
    print(lst)  