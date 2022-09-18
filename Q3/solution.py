class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        list1 = nums1 + nums2

        list1.sort()

        start = 0
        end = len(list1) - 1

        mid = (start+end)//2

        if len(list1) % 2 != 0:
            return list1[mid]

        return (list1[mid] + list1[mid+1]) / 2
        
