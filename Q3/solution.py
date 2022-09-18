def median(num1, num2):
  
  num1.extend(num2)   # Merging the two lists
  num1.sort()         # Sorting the merged list
  middle_element = len(num1) // 2     # finding the middle element 
  if len(num1) % 2 == 0:             
    return (num1[middle_element] + num1[middle_element- 1])/2   # returning the median of even length list
  else:
    return num1[middle_element]         # returning the median of odd length list

