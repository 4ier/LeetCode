class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output

def main():
    sln = Solution()
    arrays = [[1,3],[2,4,5,6,7],[1,2],[3,4]]
    for array in arrays:
    	print array
        print sln.productExceptSelf(array)
        print "--------"

if __name__ == "__main__":
    main()
