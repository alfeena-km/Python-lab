def pattern(n) :
    for i in range(n) :
        for j in range(i):
           print('*',end =" ")
        print(' ')
n = int(input("Enter the number of rows: "))
pattern(n)
