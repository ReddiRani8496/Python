x,y,z="one","two","three"

print(x)
print(y)
print(z)

# when all variables have same value
num1 = num2 = num3 = 10;

print(num1)
print(num2)
print(num3)

print(num1 + num2 + num3) # 30

print(x+" " + y +" " + z) #one two three

#print(num1 + x) # throws error we can't concatenate of two different types of variables

# change the type of num1 to string and concatenate with x
print(str(num1) + " " + x) # 10 one