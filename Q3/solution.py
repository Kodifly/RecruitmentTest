
class Solution:
    def __init__(self) -> None:
        pass

    def findMedianSortedArrays(self, nums1: list, nums2: list) -> float:
        nums1.extend(nums2)
        n = sorted(nums1)
        index = int((len(n) + 1)/ 2)
        if len(n) % 2 == 0:
            index2 = index + 1
            median_value = (n[index-1] + n[index2-1])/2
        else:
            median_value = n[index - 1] 
        return median_value

if __name__ == '__main__':
    sol = Solution()
    num1 = [1, 3]
    num2 = [2]
    print(sol.findMedianSortedArrays(num1, num2))
    num1 = [1, 2]
    num2 = [3, 4]
    print(sol.findMedianSortedArrays(num1, num2))
    num1 = [1, 2, 4, 6]
    num2 = [3, 6, 7, 8]
    print(sol.findMedianSortedArrays(num1, num2))