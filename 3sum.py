class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        print(nums)

        result = []

        for i in range(len(nums) - 2):
            if(i>0 and nums[i]==nums[i-1]):continue
            # print([nums[i], nums[i+1], nums[i+2]])
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r = r - 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l = l + 1
                else:
                    if (l > i + 1) and (nums[l] == nums[l - 1]):
                        l = l + 1
                        continue
                    else:
                        result.append([nums[i], nums[i+1], nums[i+2]])
                        l = l + 1

        return result

def main():
    sln = Solution()
    print(sln.threeSum([-1, 0, 1, 2, -1, -4]))

if __name__ == '__main__':
    main()