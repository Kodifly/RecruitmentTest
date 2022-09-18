list_1 = [1,2]
list_2 = [3,4,5]

def findMedianSortedArrays(list_1, list_2):
    n = len(list_1)
    m = len(list_2)
    j = 0
    k = 0
    sorted_list = []
    
    for i in range(m+n):
        if j >= n and k < m:
            sorted_list = sorted_list + (list_2[k:])
            break
        elif k >= m and j < n:
            sorted_list = sorted_list + (list_1[j:])
            break
        elif list_1[j] <= list_2[k]:
            sorted_list.append(list_1[j])
            j = j + 1
        else:
            sorted_list.append(list_2[k])
            k = k + 1
    
    index = len(sorted_list)//2
    print(sorted_list)
    if len(sorted_list)%2 == 0:
        return (sorted_list[index] + sorted_list[index-1])/2
    else:
        return sorted_list[index]
        
        
print(findMedianSortedArrays(list_1, list_2))