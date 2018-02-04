class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str == '':
            return 0

        i = 0
        intCharArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        optArray = ['-', '+']
        opt = ''
        while i < len(str) and str[i] not in intCharArray\
                and str[i] not in optArray:
            print('filterd: ' + str[i])
            if str[i] != ' ':
                return 0
            i += 1

        numArray = ''
        if i < len(str) and str[i] in optArray:
            print('opt is: ' + str[i])
            opt = str[i]
            i += 1
        while i < len(str) and str[i] in intCharArray:
            numArray += str[i]
            print('insert: ' + str[i])
            i += 1
        if numArray == '':
            return 0
        ret = int(opt + numArray)

        if ret > 2147483647:
            ret = 2147483647
        if ret < -2147483648:
            ret = -2147483648
        return ret


def main():
    sln = Solution()
    print(sln.myAtoi("    010"))


if __name__ == '__main__':
    main()
