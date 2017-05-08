class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1, len2 = len(nums1), len(nums2)
        if len1 > len2:
            len1, len2, nums1, nums2 = len2, len1, nums2, nums1
        if len2 == 0:
            return 0

        imin, imax, halfLen = 0, len1, (len1 + len2 + 1) / 2
        while imin <= imax:
            i = (imin + imax) / 2
            j = halfLen - i

            if i < len1 and nums2[j - 1] > nums1[i]:
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                imax = i - 1
            else:
                if i == 0: maxOfLeft = nums2[j - 1]
                elif j == 0: maxOfLeft = nums1[i - 1]
                else: maxOfLeft = max(nums1[i - 1], nums2[j - 1])

                if (len1 + len2) % 2 == 1:
                    return maxOfLeft

                if i == len1: minOfRight = nums2[j]
                elif j == len2: minOfRight = nums1[i]
                else: minOfRight = min(nums2[j], nums1[i])

                return (maxOfLeft + minOfRight) / 2.0

def main():
    sln = Solution()
    arrays = [[[1,3],[2,4,5,6,7]],[[1,2],[3,4]]]
    for array in arrays:
        print array[0], array[1]
        print sln.findMedianSortedArrays(array[0],array[1])
        print "--------"

if __name__ == "__main__":
    main()
