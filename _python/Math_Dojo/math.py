class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in range(len(nums)):
            self.result += nums[i]
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in range(len(nums)):
            self.result -= nums[i]
        return self


md = MathDojo()
x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(md.add(2, 5, 4, 3).result)
print(md.add(12, 15, 14, 13).result)
print(md.add(22, 25, 24, 23).result)
print(md.subtract(2, 3, 4, 5).result)
print(md.subtract(12, 13, 14, 15).result)
print(md.subtract(22, 23, 24, 25).result)
print(x)
