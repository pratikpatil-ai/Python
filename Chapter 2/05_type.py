a = 31
t = type(a) # <class 'int'>

print(t)

a = "Pratik"
t = type(a) # <class 'str'>

print(t)

a = 31.2
t = type(a) # <class 'float'>

print(t)

a = "31.2"
b =  float(a) # but the type should be float
t = type(b)

print(t)