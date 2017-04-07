import random
a=[]

while len(a)<5:
	x=random.randrange(1,91)
	if x not in a:
		a.append(x)
print(a)
