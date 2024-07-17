import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

y = datetime.datetime(2018, 6, 1)

print(y.strftime("%B"))