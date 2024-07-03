# convert the tuple to a list after removing the item, convert back to tuple

marks = (80,92,75,60,85)

print(marks);

# convert tuple to list
marks_list = list(marks);

# remove 75
marks_list.remove(75);

# convert list back to tuple
marks = tuple(marks_list);

print(marks);


del marks
print(marks) # error because we are deleting the tuple