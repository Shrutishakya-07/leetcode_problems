class Solution(object):
    def fizzBuzz(self, n):
        self=[]
        for i in range(1, n+1):
            if i%3==0 and i%5==0:
                self.append("FizzBuzz")
            elif i%3==0:
                self.append("Fizz")
            elif i%5==0:
                self.append("Buzz")
            else:
                self.append(str(i))
        return self
