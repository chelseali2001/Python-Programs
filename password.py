import random

a = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890!@#$%^&*()?"

passlen = 8

p = "".join(random.sample(a, passlen))

print(p)
