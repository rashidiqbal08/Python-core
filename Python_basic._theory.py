# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

## if you want to print multiple value after decimal like 24.000(use '%.2f'%a)


#we can use any() fuction if we want to chen if any of the element lies in our conditon or not. using for loop


s=set()
i=int(input("enter the no"))
for i in range(0,i):
    s.update(input("enter the string:").split())

print(s)
print(len(s))