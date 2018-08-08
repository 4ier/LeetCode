class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) < 2:
            return 1
        
        index = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[index]:
                index = index + 1
                nums[index] = nums[i]

        return index + 1

def main():
    sln = Solution()
    ipt = [[[1,1,2], 2],[[0,0,1,1,1,2,2,3,3,4],5]]
    for arr, result in ipt:
        print('-----')
        print(arr)
        value = sln.removeDuplicates(arr)
        print value
        if result == value:
            print('passed')
        else:
            print('failed')

if __name__ == '__main__':
    main()