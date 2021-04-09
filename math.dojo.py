class MathDojo:
  def __init__(self):
    self.result = 0
  def add(self, num, *nums):
    self.result += num 
    for number in nums:
      self.result += number
    return self
  def subtract(self, num, *nums):
    self.result -= num
    for number in nums:
      self.result -= number
    return self

md = MathDojo()
# para probar:
#x = md.add(2).add(2,5,1).subtract(3,2).result
#x = md.add(4).add(9,10,1).subtract(4,5).result
x=md.add(10,20,10).add(5).subtract(100).result
print(x)	
