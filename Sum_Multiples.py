class Solution(object):
    def sumOfMultiples(self, n):
        self=0
        for i in range(1,n+1):
            if i%3==0 or i%5==0 or i%7==0:
                self=self+i
        return self
