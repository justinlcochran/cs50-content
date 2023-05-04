import math

class Calculator():
    def __init__(self, mode):
        self.mode = mode

    def add(self, number_one, number_two):
        return number_one + number_two

    def subtract(self, number_one, number_two):
        return number_one - number_two

    def multiply(self, number_one, number_two):
        return number_one * number_two

    def divide(self, number_one, number_two):
        return number_one / number_two

    def exponentiate(self, number_one, number_two):
        return number_one ** number_two

    def sine(self, number):
        if self.mode == 'radians':
            return math.sin(number)
        elif self.mode == 'degrees':
            return math.sin(number * ((2 * math.pi)/360))






'''
1. Allow for a third mode called "round" that rounds all answers and
    returns an integer response.

2. Demonstrate that this new feature works with addition,
    subtraction, multiplication, division, and exponentiation.

3. Add a final method called "percentage" that takes a number and
    a percentage (as a string, '15%'),then calculates that
    percentage of the original number.

4. In your percentage method, return a sentence explaining
    that the answer is x% of the number.
'''

