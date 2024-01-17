class Vector:
    def __init__(self, nums):
        self.nums = nums
        

    def is_not_same_len(self, first, second):
          return len(first.nums) == len(second.nums)


    def add(self, other):
        if self.is_not_same_len(self, other):
            return Vector([first + second 
                           for first, second 
                           in zip(self.nums, other.nums)])
        raise IndexError("Unequal lengths")


    def subtract(self, other):
        if self.is_not_same_len(self, other):
            return Vector([first - second 
                           for first, second 
                           in zip(self.nums, other.nums)])
        raise IndexError("Unequal lengths")
    

    def dot(self, other):
        if self.is_not_same_len(self, other):
            return sum([first * second 
                        for first, second 
                        in zip(self.nums, other.nums)])
        raise IndexError("Unequal lengths")
    

    def norm(self):
        return sum([first ** 2 
                    for first 
                    in self.nums]) ** 0.5



    def equals(self, other):
        return self.nums == other.nums
    

    def __str__(self):
        return f"{tuple(self.nums)}"



a = Vector([1, 2])
b = Vector([3, 4])

print(a)