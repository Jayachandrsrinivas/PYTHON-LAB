n = int(input("Enter the number"))
count = 0

for i in range(2,n):
    if(n%2 == 0):
        count = 1
        break
    if(count == 1):
        print("it not a prime")
else:
    print( "it is  prime" )
