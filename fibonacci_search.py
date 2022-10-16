
#Function to sort the array
def sort(a):
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[j] < a[i]:
                a[j],a[i]=a[i],a[j]
    return a

#Function to accept rollnumber
def accept():
    arr = []
    n = int(input("Enter number of students who attended the training program :"))
    for i in range (n):
        ask = int(input("enter rollnumber of student %d :"%(i+1)))
        arr.append(ask)
    print("all entries successful!!")
    return arr

#Fibonacci Search
def fibonacci_search(A,x):
    f1 = 0
    f2 = 1
    f3 = f1 + f2
    n = len(A)
    offset = -1
    while (f3 < len(A)):
        f1=f2
        f2 = f3
        f3 = f1 + f2
    while (f3>1):
        i = min(offset+f2,n-1)
        if x == A[i]:
            return i
        else:
            if (x < A[i]):
                f3 = f1
                f2 = f2 - f1
                f1 = f3 - f2
                offset = offset
            else:
                f3 = f2
                f2 = f1
                f1 = f3 - f2
                offset = i
        if (f2 == 1 and (offset+1)<n and A[offset+1]==x):
            return offset +1
    return -1

#Main function
to_con = 'y'
while (to_con == 'y'):
    print("press 1 to enter marks of student")
    print("press 2 to check whether a student attended the program or not")
    ask = int(input("enter your choice : "))
    if (ask == 1):
        a = accept()
    elif (ask == 2):
        a = sort(a)
        k = fibonacci_search(a)
        if (k == -1):
            print("student not present in the program")
        else:
            print("student present in the program at index ",k,"in sorted list")
    else:
        print("wrong input..try again")
    to_con = input("do you want to continue (y/n) : ")