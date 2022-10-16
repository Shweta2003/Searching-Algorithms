#Function to accept rollnumber
def accept():
    arr = []
    n = int(input("Enter number of students who attended the training program :"))
    for i in range (n):
        ask = int(input("enter rollnumber of student %d :"%(i+1)))
        arr.append(ask)
    print("all entries successful!!")
    return arr

#Function of linear search
def linear_search(a):
    find = int(input("enter rollnumber of student to find :"))
    for i in range(len(a)):
        if (a[i] == find):
            return i
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
        k = linear_search(a)
        if (k == -1):
            print("student not present in the program")
        else:
            print("student present in the program at index ",k)
    else:
        print("wrong input..try again")
    to_con = input("do you want to continue (y/n) : ")
