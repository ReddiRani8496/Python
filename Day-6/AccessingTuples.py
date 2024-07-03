marks = (80,92,75,60,85)

print(marks[0]) # returns first element 80

print(marks[1]) # returns second element 92

print(marks[-1]) # negative indexing starts from right to left, it will return 85

print(marks[1:]) # if we don't specify the ending index then it will consider 1st index to last index

print(marks[:3]) # if we don't specify the starting index then it will consider starting index to specified index

print(marks[1:4]) # it will return 1st, 2nd and 3rd. 4th index is exclusive


if 75 in marks:
    print("75 exists in marks tuple")