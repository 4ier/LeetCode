class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        str = "1"
        i = 0
        while i < n - 1: 
            str = self.say(str)
            i += 1
        
        return str

    def say(self, str2Say):
        lastChar = str2Say[0]
        returnStr = ""
        count = 1
        for char in str2Say[1:]:
            if lastChar == char:
                count += 1
            else:
                returnStr += str(count)
                returnStr += lastChar
                count = 1
            lastChar = char
        return returnStr + str(count) + lastChar

def main():
    sln = Solution()
    print(sln.countAndSay(4))

if __name__ == '__main__':
    main()