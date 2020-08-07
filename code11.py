a = range(int(input("enter a number")),int(input("enter a number"))+1)
for j in a:
    for i in range(1, 11):
        print(j, "x", i, "=", i*j)
