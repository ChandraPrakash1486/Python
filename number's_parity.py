def a():
    list1  = []
    list2 = []
   
    y = int(input("Enter the Range: "))
    for i in range(y):
        if (i%2==0):
            list1.append(i)
        else:
            list2.append(i)
    

    print("Even Numbers: ",list1)
    print("Odd Numbers: ",list2)
a()
