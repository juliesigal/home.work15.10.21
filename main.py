===========targil 8 page 38:

line = int(input("please enter a number"))
stand = int(input("please enter a number"))

for i in range(1,line+1):
    print("* "*stand)
    
===========targil 1 page 35:

num = int(input("please enter a number"))
min = num

for i in range(1,100):
    num = int(input("please enter a number"))
    if num < min:
        break
    else:
        min = num

if i == 99:
    print("sorted")
else:
    print("not sorted")
    
===========targil 16 page 26:


x = int(input("please enter a number"))
y = int(input("please enter a number"))
result = 0

for i in range(1,y+1):
    result = result + x

print(result)
