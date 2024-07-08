def print_age(*,age):
    print(f"Age: {age}")

# print_age(20) # will throw error, we need to pass argument as key value pair

print_age(age=20) # valid

