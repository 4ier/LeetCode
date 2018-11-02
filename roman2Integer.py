class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numMap = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

        total = 0
        prev = 0
        for char in s[::-1]:
            curr = numMap[char]
            if curr < prev:
                total -= curr
            else:
                total += curr
            prev = curr
        return total


        
def main():
    sln = Solution()
    ipt = [["I", 1],["V",5],["IV",4]]
    for arr, result in ipt:
        print('-----')
        print(arr)
        value = sln.romanToInt(arr)
        if result == value:
            print('passed')
        else:
            print('failed')

if __name__ == '__main__':
    main()