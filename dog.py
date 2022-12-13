# create class
class Dog:
    def __init__(self, name):
        self.name = name
        self.aaa = 3
        self.bbb = [1,2,3]
    
    def bark(self):
        return f"woof! my name is {self.name}"
    

# multiple objects
dogs = []
for name in ['filo', 'lassy', 'milo']:
    d = Dog(name)
    dogs.append(d)

for i,d in enumerate(dogs):
    print(f"dog {i} barking {d.bark()}")
