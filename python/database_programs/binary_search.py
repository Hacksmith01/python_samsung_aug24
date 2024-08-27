lst=[]
n=int(input("Enter the number of elements in the list: "))
for i in range(n):
    elements=int(input("Enter the liset elements"))
    lst.append(elements)

lst.sort()

search_element=int(input("Enter the elemnt to be searched for:"))
start_index=0
end_index=n-1
while start_index<=end_index:
    mid_index=(start_index+end_index)//2
    if lst[mid_index]==search_element:
        print(f"Element found at mid indeex is: {mid_index}")
        break
    elif search_element<lst[mid_index]:
        end_index=mid_index-1
    else:
        start_index=mid_index+1