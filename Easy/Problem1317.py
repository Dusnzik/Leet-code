# Given an integer n, return array [a,b] where a + b = n and neither a nor b contains any zeros.
class Solution:
    def getNoZeroIntegers(self, n: int):
        def nozero(x):
            while x>0:
                if x%10==0:
                    return False
                x//=10
            return True
        for i in range(1,n):
            if nozero(i) and nozero(n-i):
                return [i,n-i]
        