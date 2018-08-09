class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while(i < len(nums)):
            if nums[i] == val:
                del nums[i]
            else:
                i = i + 1

        # print nums
        return len(nums)

def main():
    sln = Solution()
    print sln.removeElement([0,1,2,2,2,3], 2)

if __name__ == '__main__':
    main()