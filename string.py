a="THIS IS ME"
print(a.capitalize())
This is me
print(a.upper())
THIS IS ME
print(a.lower())
this is me
print(a.title())
This Is Me
print(a.swapcase())
this is me
print(a.split())
['THIS', 'IS', 'ME']
print(a.center(19,"*"))
*****THIS IS ME****
print(a.count('this'))
0
print(a.replace('THIS','THAT'))
THAT IS ME
b="THAT"
a="_"
print(a.join(b))
T_H_A_T
a="hello"
print(a.isupper())
False
print(a.islower())
True
print(a.isalpha())
True
print(a.isalnum())
True
print(a.isdigit())
False
print(a.isspace())
False
print(a.istitle())
False
print(a.startswith("h"))
True
print(a.endswith("o"))
True
print(a.find("hello"))
0
print(len(a))
5
print(min(a))
e
print(max(a))
o
