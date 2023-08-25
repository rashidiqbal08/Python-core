##Set

# Note: Set items are unchangeable, but you can remove items and add new items.
#  Sets are unordered, so you cannot be sure in which order the items will appear.


set1={1,3,4,1}
print(set1)
for i in set1:
    print(i)


#add items
#Once a set is created, you cannot change its items, but you can add new items.

set2={'raj','sam','sahil'}
set2.add('srija')
print("set2: ",set2,type(set2))


#remove items    by remove('element') and pop() and del

set3={10,20,30,40}
x=set3.pop()
print(x)  #this 'x' will print the popped item
print(set3)    #this will print the set after popped

set3.remove(20)
print("set3: ",set3) 

# del set3
# print(set3)


#To merge two sets by  '1.update(2)' and '1.union(2)'

set4={1,2,3,4,5}
set5={6,7,8,9,10}
set4.update(set5)
print("set4: ",set4)

# print(set4.union(set5))
