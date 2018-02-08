class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        result = 0
        tmp = 0
        length = len(height)
        left = 0
        right = length - 1
        l, r = 0, 0
        while left < right:
            l, r = height[left], height[right]
            tmp = min(l, r) * (right - left)
            if result < tmp:
                result = tmp
            if l < r:
                while left < right and height[left] <= l:
                    left += 1
            else:
                while left < right and height[right] <= r:
                    right -= 1
                        
        return result


def main():
    sln = Solution()
    print(sln.maxArea([2, 3, 10, 5, 7, 8, 9]))


if __name__ == '__main__':
    main()
