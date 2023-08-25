# LOOP

# printing the only item which is int and > 6 from list

list=['Rashid Iqbal','Bhopal',1,5,8,6,True]
for i in list:
    if type(i)==int and i>=6:
        print(i)
    


#print value from 1 to 10 in range

for i in range(1,11,1):
    print("Value of i: ",i)
    
for i in range(1,10):
    print(i)
    if i==5:
        break

for i in range(1,10,1):
    if i==5:
        continue
    print(i)



#PRINTING PATTERN

# printing square

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()

#printing right triangle

# i=1
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()

# left triangle

for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()

# right slider

