from tkinter import W


class Solution:

    def findMedianSortedArrays(self, nums1, nums2) -> float:
        
        nums3 = nums1 + nums2
        nums3.sort()

        odd_or_even = len(nums3)

        if odd_or_even % 2 == 0:
            half = odd_or_even //2
            even = nums3[half]
            even_prior = nums3[half - 1]
            return (even + even_prior) /2

        else:
            half = odd_or_even //2
            return nums3[half]


if __name__ == "__main__":

    sol = Solution()
    print(sol.findMedianSortedArrays([1,3],[2]))
    print(sol.findMedianSortedArrays([1,2],[3,4]))
    
