l=[0]*5
print(len(l))
# print(l)
#this won't behave like a append
#it will override the value of zero
l=[i+1 for i in range(5)]
print(l)
#this append will keep adding the extra element after zero
for i in range(5):
    l.append(i+1)
print(l)