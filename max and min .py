l = []
n = int(input("enter the size of list"))

for i in range(n):
	val = int(input("enter the elements"))
	l.append(val)
print("min value",l.index(min(l)))
print("max value",l.index(max(l)))
