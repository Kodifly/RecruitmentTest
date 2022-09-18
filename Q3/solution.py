from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        if length % 2 == 1:   # if merged array has odd length return middle element
            return self.findMedian(nums1, nums2, length // 2)
        else:   # if even length then return (middle + middle - 1)/2
            return (self.findMedian(nums1, nums2, length // 2) + self.findMedian(nums1, nums2, length // 2 - 1)) / 2

    def findMedian(self, nums1, nums2, mid):
        if not nums1:   # if first array is empty just consider second array
            return nums2[mid]
        if not nums2:
            return nums1[mid]
        i_nums1, i_nums2 = len(nums1) // 2, len(nums2) // 2
        m_nums1, m_nums2 = nums1[i_nums1], nums2[i_nums2]

        # if mid is bigger than the sum of nums1 and nums2's median indices
        if i_nums1 + i_nums2 < mid:
            # if nums1's median is bigger than nums2's, nums2's first half doesn't include mid
            if m_nums1 > m_nums2:
                return self.findMedian(nums1, nums2[i_nums2 + 1:], mid - i_nums2 - 1)
            else:
                return self.findMedian(nums1[i_nums1 + 1:], nums2, mid - i_nums1 - 1)
        # when mid is smaller than the sum of nums1 and nums2's indices
        else:
            # if nums1's median is bigger than nums2's, nums1's second half doesn't include mid
            if m_nums1 > m_nums2:
                return self.findMedian(nums1[:i_nums1], nums2, mid)
            else:
                return self.findMedian(nums1, nums2[:i_nums2], mid)
