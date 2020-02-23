
#剑指第12题
#给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
#保证base和exponent不同时为0
class Solution:
    def Power(self, base, exponent):
        # write code here
        if exponent>0:
            base_1=base
            for i in range(exponent-1):
                base_1=base_1*base
            return base_1
        elif exponent<0:
            base=1/base
            base_1=base
            exponent=abs(exponent)
            for i in range(exponent-1):
                base_1 = base_1 * base
            return base_1
        else:
            return 1



solution=Solution()
answer=solution.Power(2,5)
print(answer)

#调试成功！