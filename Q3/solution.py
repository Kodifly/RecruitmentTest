class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1+nums2)%2!=0: # check the length of the solution 
            return sorted((nums1+nums2))[len(nums1+nums2)//2]/1 # Simple code to return the median if the length is odd
        else:
            return sum(sorted((nums1+nums2))[(len(nums1+nums2)//2)-1:(len(nums1+nums2)//2)+1])/2 # Simple code to return the median if the length is even.
        #It is not efficient code. but easy to understand and simplest approach to my knowledge.
        
        
# in this case runtime increases but its memory efficient.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        half = (len(nums1) + len(nums2))
        idx = 0
        idy = 0
        
        while True:
            
            if idx == len(nums1):
                a += nums2[idy:]
                break
            elif idy == len(nums2):
                a += nums1[idx:]
                break
            if nums1[idx] < nums2[idy]:
                a.append(nums1[idx])
                idx += 1
            else:
                a.append(nums2[idy])
                idy += 1
        return a[half // 2] if half % 2 != 0 else (a[half //2] + a[(half - 1) // 2]) / 2
    # While this one is more efficient,.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = []
        half = (len(nums1) + len(nums2))

        
        while nums1 and nums2:
            if nums1[0] < nums2[0]:
                a.append(nums1.pop(0))
            else:
                a.append(nums2.pop(0))
        
        a += nums1 + nums2

        return a[half // 2] if half % 2 != 0 else (a[half //2] + a[(half - 1) // 2]) / 2
        
