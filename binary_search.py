
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

#function of binary search
def binary_search(a):
    find = int(input("enter rollnumber of student to find :"))
    low = 0
    high = len(a) - 1
    
    while (low <= high) :
        mid = int((low + high)/2)
        if (a[mid] == find):
            return mid
        else:
            if (find < a[mid]):
                high = mid - 1
                
            else:
                low = mid + 1
            
    else:
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
        k = binary_search(a)
        if (k == -1):
            print("student not present in the program")
        else:
            print("student present in the program at index ",k,"in sorted list")
    else:
        print("wrong input..try again")
    to_con = input("do you want to continue (y/n) : ")
