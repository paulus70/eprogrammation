#exemple de sequence X se trouvant dans le projet de tri 
x= [20, 10, 15, 10, 12, 5, 8, 12, 9, 4, 1]

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
            #print(myList)
        else:
            # swap places
            memo=myList[left]
            myList[left]=myList[right]
            myList[right]=memo
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        split = partition(myList, start, end)
        # sort both halves
        quicksort(myList, start, split-1)
        quicksort(myList, split+1, end)
    return myList

print ("before", x)
quicksort (x,0,len(x)-1)
print ("after", x)
