#FUNCTION

# In python, the function definition should always be present before the function call.
#  Otherwise, we will get an error.

# DOCSTRING-It is briefly used to explain what a function does.

def hello(name):
    """this will return hello with name"""
    return "hello " +name+" good morning"
   

print(hello("Rashid"))

def per(a,b,c):
    """this function will calculate the
    percentage of student"""
    print("Total attendance of {} are".format(c) ,(b/a)*100)


a=int(input("Enter the total no of days."))
b=int(input("Enter the no of days present"))
per(a,b,"Rashid")


#We can also use augument as key value pair(order does not matter.)

def aiml_sub(a,b,c):
    print("The subjects of aiml branch: ",a,b,c)

aiml_sub(c="artificial intelligence", a="machine learning", b="Data science.")


# #return vs print in function
# - if we're using return then we have to use print with call
# - but if we use print inside func then we'll get output after just calling

def add(a,b):
    return a+b

print(add(5,3))

def add2(a,b):
    print("The sum is: ",a+b)

add2(5,6)


fuction to print the last char of string
def last(name):
    return name[-1]

print(last("Rashid"))

#func for odd even

def odd_even(num):
    if num%2==0:
        return True  #return "even"
    else:
        return False    #return "odd"

print(odd_even(14)) 

#this will just give true or false
def is_even(num):
    return num%2==0

print(is_even(13))


# func to print the greatest of three

def great(a,b,c):
    if a>b:
        if a>c:
            return a, "is greatest"
        return c, 'is greatest'
    else:
        if b>c:
            return b, "is greatest"
        return c, 'is greatest'

print(great(45, 55,8)) 


#function for palindrome

def pal(string):
    x=string[::-1]
    if x==string:
        return True
    return False

print(pal("madam"))


#check int is palindrom or not


def pal_num(num):
    a=num

    #code to reversed an integer
    store=0
    while a!=0:
        r= a%10
        store= (store*10) +r
        a= a//10
    print("reversed no", store)
    print("original int", num)

    #comparing the original value and reversed one.
    if num==store:
        return True
    return False
    

print(pal_num(232))


