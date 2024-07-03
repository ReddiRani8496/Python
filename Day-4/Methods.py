str = "Hello World"

print(len(str)) # returns length of string

print(str.upper()) # returns upper case string

print(str.lower()) # returns lower case string

print(str.capitalize()) # returns first character as uppercase and others as lowercase


# replace method replaces all occurrences of a substring with another substring
print(str.replace("World", "Python")) # Hello Python


# split method splits a string into a list of substrings based on a delimiter
print(str.split(" ")) # ['Hello', 'World']

# strip method removes the space at the beginning and ending of string
print(str.strip()) # Hello World