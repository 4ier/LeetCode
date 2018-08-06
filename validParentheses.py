class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        matchPairs = {
            '(':')',
            '[':']',
            '{':'}',
            ')':'(',
            ']':'[',
            '}':'{'}

        stack = []
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if stack and matchPairs[stack[-1]] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return 0 == len(stack)
        
def main():
    sln = Solution()
    ipt = [['()', 1],['(){}[]', 1],['([)]', 0]]
    for arr, result in ipt:
        print('-----')
        print(arr)
        value = sln.isValid(arr)
        print(value)
        if result == value:
            print('passed')
        else:
            print('failed')

if __name__ == '__main__':
    main()