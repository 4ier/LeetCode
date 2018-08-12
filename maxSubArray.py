class Solution(object):
    def maxSubArray1(self, nums): # 效率太低o(n^2)
        """
        :type nums: List[int]
        :rtype: int
        """

        # subNums = []
        summ = nums[0]

        for bIndex in range(len(nums)):
            for eIndex in range(1, len(nums[bIndex:]) + 1):
                tmp = sum(nums[bIndex:bIndex + eIndex])
                if tmp > summ:
                    summ = tmp
                    # subNums = nums[bIndex:bIndex + eIndex]
        # print(subNums)
        return summ

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curIndex = 0
        curSum = maxSum = nums[0]
        for index,num in enumerate(nums[1:]):
            if num > curSum + num:
                curIndex = index + 1
            curSum = sum(nums[curIndex: index + 2])
            maxSum = max(maxSum, curSum)
        return maxSum

def main():
    sln = Solution()
    print(sln.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))

if __name__ == '__main__':
    main()