import sys

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        MIN_VAL = -1 * sys.maxsize -1
        MAX_VAL = sys.maxsize
        imin, imax, half_len = 0, m, (m + n + 1)//2
        while imin <= imax:
            i = (imin + imax)//2
            j = half_len - i

            max_1 = MIN_VAL if i == 0 else nums1[i-1]
            min_1 = MAX_VAL if i == m else nums1[i]

            max_2 = MIN_VAL if j == 0 else nums2[j-1]
            min_2 = MAX_VAL if j == n else nums2[j]

            if max(max_1, max_2) <= min(min_1, min_2):
                if (m + n) % 2 == 0:
                    return (max(max_1, max_2) + min(min_1, min_2))/2
                else:
                    return max(max_1, max_2)
            elif max_1 > min_2:
                imax = i - 1
            else:
                imin = i + 1
