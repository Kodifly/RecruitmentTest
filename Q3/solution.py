class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        le1, le2 = len(nums1), len(nums2)
        total = le1 + le2 
        half = total // 2
        if le1 < le2:
            return self.findMedianSortedArrays(nums2, nums1)
        l, r = 0, len(nums1) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            aleft = nums1[i]
            aright = nums1[i+1]
            bleft = nums1[j]
            bright = nums1[j+1]
        
            if aleft <= bright and bleft <= aright:
                if total % 2 == 0:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1