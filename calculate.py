class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        print '-------------'
        result, offset = self.subCalc(s)
        return result

    def subCalc(self, s):
        num = ''
        offset = 0
        numArray = []
        optArray = []
        for index, char in enumerate(s):
            if offset < 0:
                offset = offset + 1
                print 's ', s
                print 'char ', char
                print 'offset ', offset
                continue

            if str(char).isalnum():
                num += char
            else:
                if num != '':
                    numArray.append(int(num))
                num = ''
                if char == '(':
                    num, offset = self.subCalc(s[index + 1:])
                elif char == ')':
                    return self.calc(numArray, optArray), 0 - index
                elif char == ' ':
                    pass
                else:
                    optArray.append(char)
        if num != '':
            numArray.append(int(num))

        return self.calc(numArray, optArray), 0

    def calc(self, numArray, optArray):
        result = int(numArray[0])
        print numArray
        print optArray
        for index, opt in enumerate(optArray):
            if opt == '+':
                result = result + int(numArray[index + 1])
            else:
                result = result - int(numArray[index + 1])

        return str(result)


def main():
    sln = Solution()

    #ipt = [["1 + 1", 2], [" 2-1 + 2 ", 3], ["(1+(4+5+2)-3)+(6+8)", 23]]
    ipt = [["(1+(4+5+2)-3)+(6+8)", 23]]
    for arr, result in ipt:
        value = int(sln.calculate(arr))
        if result == value:
            print 'passed'
        else:
            print 'failed'

if __name__ == '__main__':
    main()
