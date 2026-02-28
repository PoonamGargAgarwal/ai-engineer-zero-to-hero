# Create a list which stores the first n natural numbers and import class from problem1.py to test the functions of mean, median and mode
from day3.problem1 import NaturalNumbers
class List(NaturalNumbers):
    def __init__(self,n):
        super().__init__(n)

    def get_list(self):
        self.create_list()
        return self.natural_numbers
    
    def print_list(self):
        return super().print_list()
    
    def is_empty(self):
        return len(self.natural_numbers) == 0
    
    def mergelist(self, other_list):
        for num in other_list.natural_numbers:
            self.natural_numbers.append(num)
        self.n += other_list.n  
     
    def commonElements(self, other_list):
        common = []
        for num in self.natural_numbers:
            if num in other_list.natural_numbers and num not in common:
                common.append(num)
        return common

