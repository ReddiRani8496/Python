marks = (80,92,75)

(maths,science,social) = marks;

print(maths);
print(science);
print(social);

# assigning multiple variables in one line using tuple unpacking.

marks_list = (80,92,75,60,85);

(maths, *others) = marks_list;

print(maths);
print(others); # returns a tuple with 92,75,60,85