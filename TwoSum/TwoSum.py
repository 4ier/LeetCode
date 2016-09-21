#coding=utf-8
'''
https://leetcode.com/problems/two-sum/
'''
class Solution(object):
    def twoSum(self, nums, target):
	    """
	    :type nums: List[int]
	    :type target: int
	    :rtype: List[int]
	    """
	    dic = {}	    
	    for x in range(0,len(nums)):
	    	dif = target - nums[x]
	    	if dic.has_key(dif):
	    		return [dic.get(dif), x]
	    	else:
	    		dic[nums[x]] = x