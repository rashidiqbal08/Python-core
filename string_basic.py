#here we will code all the basics of string.
#STRINGS ARE IMMUTABLE CAN'T BE CHANGE OR UPDATE.
string1 = "I am Rashid Iqbal."
print(string1)


#Accessing the character in string using indexing.

string2="Pythoncode"
print(string2[1])
print(string2[-1])

#slicing an string

print(string2[0:10])
print(string2[2:7])
print(string2[1:-1]) #till second last
print(string2[0:10:2]) #with gap of each character


#reversing a string

string3='SHRIJA JHA'

#we can reverse the string while accesing the char.
print(string3[::-1])

#and also by join function
string3="".join(reversed(string3))
print(string3)

#deleting an string

# del string3
# print(string3)


#Formatting of strings using .format()

#position formatting
string4="{} {} {}".format('Name','Rashid','Iqbal')
print(string4)

#keyword formatting
string4="{i} {j} {k}".format(i="name",j="Rashid",k='Iqbal')
print(string4)


#spliting and join a string

s="Rashid is handsome"
print(s)
x=s.split(" ")     #it will convert string into list
print(x)
print("-".join(x))  #joining the splitted string
