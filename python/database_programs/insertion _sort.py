
lst = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    element = int(input("Enter a list element: "))
    lst.append(element)

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j =j - 1 
        lst[j + 1] = key

insertion_sort(lst)

print("Sorted list:", lst)
