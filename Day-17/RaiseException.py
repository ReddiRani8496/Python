#The raise keyword is used to raise an exception.

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
