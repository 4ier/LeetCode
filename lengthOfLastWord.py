class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordArray = s.split(" ")
        for word in wordArray[::-1]:
            if len(word) != 0:
                return len(word)
        return 0

def main():
    sln = Solution()
    print(sln.lengthOfLastWord("hello world  "))

if __name__ == '__main__':
    main()