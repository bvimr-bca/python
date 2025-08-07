a = 10
b = 15
c = 20
#30
temp = a + b + c
a = temp - (a + b)
b = temp - (b + c)
c = temp - (a + b)
print(a,b,c)
