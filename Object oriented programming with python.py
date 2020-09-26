# lcasse Dog
class Dog:
    
    # object class attribute
    species = "Canis familiaris"
    
    # Class instance
    def __init__(self, name, age):
        
        # instance attributes 
        self.name = name
        self.age = age
        
    # instance method 'str'
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    # instance method 'speak'
    def speak(self, sound):
        return f"{self.name} says {sound}"


#child classes
''' to create a child classes you have to put the Dog as argument'''
    
# child class JackRussellTerrier
class JackRussellTerrier(Dog):
    ''' if I want to add new sound to JackRussellTerrier class I can just add
a new instance method inside JackRussellTerrier, as following : '''
    
    def speak(self, sound= "haap"):
        return f'{self.name} says {sound}'
    
# child class Dachshund
class Dachshund(Dog):
    pass

# child class Bulldog
class Bulldog(Dog):
    pass
