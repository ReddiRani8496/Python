# we can't modify the tupple, but there is solution:
# convert tuple into a list, change the list, and convert the list back into a tuple.

marks = (80,92,75,60,85)

print(marks);

# convert tuple to list
marks_list = list(marks);

# change the value at index 2
marks_list[2] = 78;

# convert list back to tuple
marks = tuple(marks_list);

print(marks);