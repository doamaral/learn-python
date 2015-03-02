__author__ = 'Lucas'

class pet:
    number_of_legs = 0
    def sleep(self):
        print("ZZzZzzzzZZzz...")
    def count_legs(self):
        print("it has %d legs" % self.number_of_legs)

#herança
class dog(pet):
    def bark(self):
        print("Auuuf, Auuuf")

dog = dog()
dog.number_of_legs = 4
dog.count_legs()
dog.bark()
dog.sleep();

nemo = pet()
nemo.number_of_legs = 0
nemo.count_legs()
nemo.sleep();