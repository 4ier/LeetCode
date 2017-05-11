#coding=utf-8
'''
https://leetcode.com/problems/rotate-function/
'''
class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        tmp = [0]
        sumA = 0
        leng = len(A)
        for x in xrange(0,leng):
    		tmp[0] = tmp[0] + x * A[x]
    		sumA = sumA + A[x]

    	result = tmp[0]
        for y in xrange(1,leng):
        	tmp.append(tmp[y - 1] + sumA - leng * A[leng - y])
        	if tmp[y] > result:
        		result = tmp[y]

        return result

#test case
if __name__ == '__main__':
	sln = Solution()
	print sln.maxRotateFunction([4,3,2,6])
