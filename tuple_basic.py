# ##tuple
# Tuples are used to store multiple items in a single variable.
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

tup1=("Redmi","Realme",25.5,True,"Vivo","Oppo")
print(tup1)

#it allow duplicate values
tup2=(2,4,1,2)
print(tup2)
print(type(tup2))


#we can also use tuple constructor tuple()
T = tuple(('raj','raju','sam'))
print(T)
print(type(T))


#accessing the element in tuple

tup3=(2,3,4,5,1)
print("tup3:- ",tup3[2])
print(tup3[1:4])
print(tup3[1:])
print(tup3[0:5:2])

#negative indexing
print(tup3[0:-1])


#updating the tuple
#we can't update the tuple as it's immutable but we can
#convert it in list make change then convert back to tuple

tup4=('birani','raita','chicken','roast')
print("original tuple: ",tup4)
list1=list(tup4)
list1[1]='salad'
print(type(list1))
tup4=tuple(list1)
print(tup4)
print(type(tup4))

#We can also add two tuple


##Unpacking a Tuple
#When we create a tuple, we normally assign values to it. This is called "packing" a tuple:

tup5=('Rashid','Jay','Bhumika','anshika')

(R,J,B,A)=tup5    #here we can't assing no.
print(R)
print(J)
print(B)
print(A)


#some methods in tuple

#count() - Returns the number of times a specified value occurs in a tuple
#index() - to search the element's position