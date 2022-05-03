#Data Types, Strings, Integer, Floats Boolean(True or False)
from lib2to3.pgen2.token import EQUAL


b1=True
b2=False
print(type(b1))

knows_password=True
knows_username=True
login=knows_password and knows_username
print(type(login))
print(login)
print(not knows_password)

#Boolean operators: Not, and or

recover=knows_password or knows_username


is_raining=False
is_cold=True
print(type(is_raining))
#type(is_cold)

# Comparison operators
# ==EQUAL , !=Not Equal   >  <  >=   <=

print(10>5)
print(1>1.5)

temperature=19
print(temperature<20)

name="Camila"
if name=="Asli":
    print("hello")
elif name=="Camila":
    print(f"hello {name}, what are you doing")
else:
    print("woe nice to meet you")

temperature=16
windchill=3
is_raining=False

if is_raining:
    print("take an umbrella")
else:
    print("don not take umbrella")

if temperature - windchill <16 and is_raining:
    print("take a jumper")
elif temperature-windchill > 30:
