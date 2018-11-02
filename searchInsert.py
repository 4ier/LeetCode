class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index, num in enumerate(nums):
            if target <= num:
                return index

        return len(nums)

        
def main():
    sln = Solution()
    print(sln.searchInsert([1,3,5,6], 0))

if __name__ == '__main__':
    main()
