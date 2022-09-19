import sys

class Solution:

    def __init__(self, nums1: 'list[int]', nums2: 'list[int]') -> None:
        self.A = nums1
        self.B = nums2


    def findMedianSortedArrays(self) -> float:
        if len(self.A) > len(self.B):
            self.A, self.B = self.B, self.A

        lengthA = len(self.A)
        lengthB = len(self.B)
        
        start = 0
        end = lengthA

        while start <= end:
            partitionA = (start + end) // 2
            partitionB = (lengthA + lengthB + 1) // 2 - partitionA

            maxLeftA = -sys.maxsize if partitionA == 0 else self.A[partitionA -1]
            maxLeftB = -sys.maxsize if partitionB == 0 else self.B[partitionB -1]

            minRightA = sys.maxsize if partitionA == lengthA else self.A[partitionA]
            minRightB = sys.maxsize if partitionB == lengthB else self.B[partitionB]

            if maxLeftA <= minRightB and maxLeftB <= minRightA:
                if (lengthA + lengthB) % 2 == 0:
                    return (max(maxLeftA, maxLeftB) +  min(minRightA, minRightB)) / 2
                else:
                    return (max(maxLeftA, maxLeftB))

            elif maxLeftA > minRightB:
                end = partitionA - 1

            else:
                start = partitionA + 1


if __name__ == "__main__":

    nums1 = [1, 3]
    nums2 = [2]
    obj = Solution(nums1, nums2)
    result = obj.findMedianSortedArrays()
    print(f"Output: {result}")