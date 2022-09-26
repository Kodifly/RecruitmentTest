from typing import List


# code taken from geeks for geeks website and tweaked : https://www.geeksforgeeks.org/median-of-two-sorted-arrays-of-different-sizes/
class Solution:
    # A utility function to find median of two integers
    def medianOfTwoElements(self, a, b):
        return (a + b) / 2

    # A utility function to find median of three integers
    def medianOfThreeElements(self, a, b, c):

        return a + b + c - max(a, max(b, c)) - min(a, min(b, c))

    # A utility function to find a median of four integers
    def medianOfFourElements(self, a, b, c, d):
        Max = max(a, max(b, max(c, d)))
        Min = min(a, min(b, min(c, d)))
        return (a + b + c + d - Max - Min) / 2

    # Utility function to find median of single array
    def medianOfSingleArray(self, arr, n):
        if (n == 0):
            return -1
        if (n % 2 == 0):
            return (arr[n / 2] + arr[n / 2 - 1]) / 2
        return arr[n / 2]

    def findMedianUtil(self, A, N, B, M):

        # If smaller array is empty, return median from second array
        if (N == 0):
            return self.medianOfSingleArray(B, M)

        # If the smaller array has only one element
        if (N == 1):

            # Case 1: If the larger array also has one element,
            # simply call MO2()
            if (M == 1):
                return self.medianOfTwoElements(A[0], B[0])

            # Case 2: If the larger array has odd number of elements,
            # then consider the middle 3 elements of larger array and
            # the only element of smaller array. Take few examples
            # like following
            # A = {9}, B[] = {5, 8, 10, 20, 30} and
            # A[] = {1}, B[] = {5, 8, 10, 20, 30}
            if (M & 1 != 0):
                return self.medianOfTwoElements(B[M / 2], self.MO3(A[0], B[M / 2 - 1], B[M / 2 + 1]))

            # Case 3: If the larger array has even number of element,
            # then median will be one of the following 3 elements
            # ... The middle two elements of larger array
            # ... The only element of smaller array
            return self.medianOfThreeElements(B[M // 2], B[M // 2 - 1], A[0])

        # If the smaller array has two elements
        elif (N == 2):

            # Case 4: If the larger array also has two elements,
            # simply call MO4()
            if (M == 2):
                return self.medianOfFourElements(A[0], A[1], B[0], B[1])

            # Case 5: If the larger array has odd number of elements,
            # then median will be one of the following 3 elements
            # 1. Middle element of larger array
            # 2. Max of first element of smaller array and element
            # just before the middle in bigger array
            # 3. Min of second element of smaller array and element
            # just after the middle in bigger array
            if (M & 1 != 0):
                return self.medianOfThreeElements(B[M / 2], max(A[0], B[M / 2 - 1]), min(A[1], B[M / 2 + 1]))

            # Case 6: If the larger array has even number of elements,
            # then median will be one of the following 4 elements
            # 1) & 2) The middle two elements of larger array
            # 3) Max of first element of smaller array and element
            # just before the first middle element in bigger array
            # 4. Min of second element of smaller array and element
            # just after the second middle in bigger array
            return self.medianOfFourElements(B[M / 2], B[M / 2 - 1], max(A[0], B[M / 2 - 2]), min(A[1], B[M / 2 + 1]))

        idxA = (N - 1) / 2
        idxB = (M - 1) / 2

        ''' if A[idxA] <= B[idxB], then median must exist in
            A[idxA....] and B[....idxB] '''
        if (A[idxA] <= B[idxB]):
            return self.findMedianUtil(A + idxA, N / 2 + 1, B, M - idxA)

        ''' if A[idxA] > B[idxB], then median must exist in
        A[...idxA] and B[idxB....] '''
        return self.findMedianUtil(A, N / 2 + 1, B + idxA, M - idxA)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        N = len(nums1)
        M = len(nums2)
        if (N > M):
            return self.findMedianUtil(nums2, M, nums1, N);
        return self.findMedianUtil(nums1, N, nums2, M)

        
