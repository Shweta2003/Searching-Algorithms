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

#Function for index selection search
def selection_search(a,g):
    find = int(input("enter rollnumber to find : "))
    n = len(a)
    index = []
    for i in range(n):
        if (i%g == 0):
            index.append(i)
    index.append(n)
    el = 0
    for j in range(len(index)):
        if (index[j] == n):
            el = index[j-1]
            break
            
        if (a[index[j]] > find):
            el = index[j-1]
            break
    for k in range(el,el+g):
        if a[k] == find:
            return k
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
        g = int(input("enter group division number for index selection search : "))
        k = selection_search(a,g)
        if (k == -1):
            print("student not present in the program")
        else:
            print("student present in the program at index ",k,"in sorted list")
    else:
        print("wrong input..try again")
    to_con = input("do you want to continue (y/n) : ")
