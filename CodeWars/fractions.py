from math import gcd

class Fraction:

    def __init__(self, numerator, denominator):
        self.top = numerator
        self.bottom = denominator
    
    #Equality test
    
    def __eq__(self, other):
        first_num = self.top * other.bottom
        second_num = other.top * self.bottom
        return first_num == second_num
        
    def __add__(self, other):
        top = (self.top * other.bottom) + (other.top * self.bottom)
        bottom = self.bottom * other.bottom
        i = gcd(top, bottom)
        return Fraction(top // i, bottom // i)
    
    def __str__(self):
        return f"outputs: {self.top}/{self.bottom}"
        
def gcd(x, y):
    if (y == 0):
        return x
    return gcd(y, x % y)
    
    
print(gcd(37, 40))
print(Fraction(1, 8) + Fraction(4, 5))