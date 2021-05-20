a=50
b=a
print(id(a))   #shows that they are pointing towards the same int point   
print(id(b))

a=40
print(id(a))

#x,y,z
x=y=z=50
print(x)
print(y)
print(z)

#multiple values in multiple variables
a,b,c=5,10,15
print(a,b,c)