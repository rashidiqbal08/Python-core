#DICTIONARY

#1- Dictionaries are used to store data values in key:value pairs.
#2- A dictionary is a collection which is ordered*, changeable and do not allow duplicates.
#3- can be referred to by using the key name.
#4- Duplicate values will overwrite existing values(2nd value will pe printed as it overwrite)
#5- The values in dictionary items can be of any data type:


dict={"Model":"Harrier",
    "Brand":"Tata",
    "Price":140000,
    "Release data": "11th Jan 2010",
    "Country":"India",
    "List of model":['harrier','nexon','altroz']
    }
dict.
print("Original dictionary")
print(dict)
for key,value in dict.items():
    print(key,':',value)

#printing type and length
print(type(dict),len(dict))
#
print(type(dict))
#access any specific key value

for i in dict.items():
    print(type(i))     #type will be tuple


#accesing using 'dict.get("Key")'
print(dict.get("Country"))

#to print the list of all the keys.. using .keys() same for values()

print(dict.keys())


#Add/update dict

#using dict name [] (we can update or add too.)
dict["Color"]= "Navy blue"
dict["Color"]= 'Balck'
dict['speed']=160
print(dict.get('speed'))
#using update()
dict.update({'speed':120})
print(dict.get('speed'))

#
print(dict)


##Remove items in dict

#1- The pop() method removes the item with the specified key name:
#2- The popitem() method removes the last inserted item
#3- The del keyword removes the item with the specified key name:
#4- The del keyword can also delete the dictionary completely:
#5- The clear() method empties the dictionary:

dict.pop('List of model')
print(dict)
dict.popitem()
print(dict)
del dict['Country']
print(dict)
dict.clear()
print(dict)
# dict.pop("Color")
# print(dict)

# dict.popitem()
# print(dict)

# del dict["Model"]
# print(dict)

# dict.clear()
# print(dict)

# del dict
# print(dict)   #error


#Make copies of dictionary

#dict.copy()

a=dict.copy()
print(a)

dict2={'name':'Rashid','age':22,'education':'Btech'}
# dict3=dict+dict2
# print(dict3)
dict1=dict.copy()
print(dict1)
#Make a copy of a dictionary with the dict() function:


#Nested dictionary

dict2={"Child 1":{
    "Name":'Nida Naaz',
    "Gender":"Female",
    "Age": 13
},
"Child 2":{
    "Name":"Arshad Iqbal",
    "Gender": "Male",
    "Age": 10
}}

# print(dict2["Child 1"])
# print(dict2["Child 2"])


for i,j in dict2.items():
    print(i,j)

Although we can also create multiple dict and merge them into one
dict3={
    "1": dict,
    "2": dict2
}

print(dict3)


#HOW CAN WE MERGE TWO DICTIONARY
D1={"Rashid":"Iqbal","Jay":"Lowanshi"}
D2={"Gagan":"Rajput","Piyush":"Magarde"}
D3=D1.copy()

1st method   Using basic iteration
for key,value in D2.items():
    print(key,value)
    D1.update({key:value})
    # D3[key]=value      #another method
print(D1)

2nd method   using update
D1.update(D2)
print(D1)

#3rd method using merge operator(|)

print(D1|D2)
print(D1)
print(D2)



for key,value in dict.items():
    print(key,' = ',value)








