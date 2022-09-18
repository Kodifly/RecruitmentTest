class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    i = 0 # Current index of input array ar1[]
    j = 0 # Current index of input array ar2[]
    n=len(nums1)
    m=len(nums2)
    m1, m2 = -1, -1
    for count in range(((n + m) // 2) + 1) :
      if(i != n and j != m) :
        if nums1[i] > nums2[j] :
          m1 = nums2[j]
          j += 1
        else :
          m1 = nums1[i]
          i += 1           
      elif(i < n) :       
        m1 = nums1[i]
        i += 1       
           # for case when j<m,
      else :
        m1 = nums2[j]
        j += 1
       # return m1 if it's lengt odd else return (m1+m2)//2
    return m1 if (n + m) % 2 == 1 else (m1 + m2) // 2
 
        
