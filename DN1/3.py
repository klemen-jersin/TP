x = input("Vnesi številko: ")
x=int(x)

y = input("Vnesi številko: ")
y=int(y)

z = input("Vnesi številko: ")
z=int(z)

print(x) 
print(type(x))
print(y) 
print(type(y))
print(z) 
print(type(z))

if x==y:
    print("prva in druga številka sta enaki")
else:
     print("prva in druga številka sta drugačni")

if z<=x:
    print("tretja komponenta je manjša ali enaka prvi")
else:
     print("tretja komponenta je večja od prve komponente")