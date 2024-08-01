column = int (input("please input the number of column: "))
for number in range(1,100):
    print(number," ",end="")
    if (number % column ) == 0:
        print("")