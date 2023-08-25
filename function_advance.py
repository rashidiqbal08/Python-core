#FUNCTION


#1- *args and **kwargs
#     when we need to pass multiple arguments(have not fixed no .)
#     that time *args is used

def func(*args,**kwargs): #we can also use any parameters
     print("\nthese are the list of cars: \n")
     for i in args:
        print(i)

     print("\nThese are the list of actor and their character.\n")
     for key,value in kwargs.items():
        print(f"{key} plays {value}.")
cars=("honda","tata","maruti","mahindra","kia","Ferrari")
#we can add as many arguments as we want using *args

hero={"Hrithik roshan": "Krrish","shahrukh khan": "Ra-One","Ranbir kapoor": "Shiva"}
func(*cars,**hero)

#basically these are the real use of *args and **kwargs



# 2- Scope, Global variable, Global keywords

#     Global variable:- its for everyone like governmonet anyone can access global var from anywhere(inside func or outside)
#     Local variable:- it can be only accessed from  inside the function, we can't access from outside.
#     if a function can't find local variable then it will go for GLOBAL variable


n="Rashid"   #GLOBAL VARIABLE

j="Hrithik"    #GLOABL
def function(name):
    n="Sammi"    #LOCAL VARIABLE
    m="Shrija"   #LOCAL VARIABLE
    print(n)

    # j=j+" Roshan"     #here we can't change global value but we can udate local one.
    #(for updating global value we have global keyword.)

    print(j)     #INSIDE FUNC WE CAN ALSO ACCESS GLOBAL VAR.

function("This is my name.")

print("this is global ",n)   #WE CAN PRINT GLOBAL EASILY
# print("this is local ",m)    #IT WON'T PRINT LOCAL VAR.


# GLOBAL KEYWORD

x=95
print("original value of global",x)
def glob():
    L=45
    L=L+5
    print("update value of local: ",L)

    # G=G+5    it won't update the global value..BUT>>>
    # print(G)
    global x

    x = x + 5
    print("Updted value of global: ",x)

glob()
print(x)



# LAMBDA FUNCTION
#     - it's just a one liner function or anonymous function

for example
def add(a,b):
    return a+b

print(add(4,2))   #will print sum of 4 and 2

sub= lambda a,b:a-b   #use of lambda function
print(sub(4,2))       #will print diff of 4 and 2

