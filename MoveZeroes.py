#coding=utf-8
'''
https://leetcode.com/problems/move-zeroes/
'''
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        needRemoveOf = []
        for x in range(0,len(nums)):
        	if nums[x] == 0:
        		needRemoveOf.append(x)

        for y in range(0,len(needRemoveOf)):
	        del nums[needRemoveOf[y] - y]
	        nums.append(0)

#test case
if __name__ == '__main__':
	sln = Solution()
	nums = [0, 1, 0, 0,0,0,0,0,0,3, 12,100,-3,0,0,50,2]
	sln.moveZeroes(nums)
	print nums
