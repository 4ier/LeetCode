class Solution(object):
    def calculate(self, s):
        if not s:
            return 0
        stack, num, sign = [], 0, "+"
        for i in xrange(len(s)):
            print 'index: ', i
            if s[i].isdigit():
                num = num*10+ord(s[i])-ord("0")
                print 'num: ',num
            if (not s[i].isdigit() and not s[i].isspace()) or i == len(s)-1:
                if sign == "-":
                    print 'appended:-num: ', -num
                    stack.append(-num)
                elif sign == "+":
                    print 'appended:num: ', num
                    stack.append(num)
                elif sign == "*":
                    t = stack.pop()
                    print 'appended:*:t = ', t, ' num = ', num
                    stack.append(t*num)
                else:
                    tmp = stack.pop()
                    print 'appended:/:t = ', tmp, ' num = ', num
                    if tmp/num < 0 and tmp%num != 0:
                        stack.append(tmp/num+1)
                    else:
                        stack.append(tmp/num)
                sign = s[i]
                num = 0
        return sum(stack)



def main():
    sln = Solution()
    ipt = [[" 3+5 / 2 ", 5],["3+2*2",7],[" 3/2 ",1]]
    for arr, result in ipt:
        print '-----'
        print arr
        value = sln.calculate(arr)
        if result == value:
            print 'passed'
        else:
            print 'failed'

if __name__ == '__main__':
    main()