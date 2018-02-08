class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        m = ["", "M", "MM", "MMM"]
        c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        x = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        i = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        return m[num / 1000] + c[(num % 1000) / 100] + x[(num % 100) / 10] + i[(num % 10)]


def main():
    sln = Solution()
    # print(sln.isPalindrome(0))
    print(sln.intToRoman(10))
    # print(sln.isPalindrome(9876789))
    # print(sln.isPalindrome(98766))


if __name__ == '__main__':
    main()
