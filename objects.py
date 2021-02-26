#Sample class

class PartyAnimal:
    x = 0
    name = ''
    
    # constructor
    def __init__(self, n=name):
        self.name = n
        print('I\'m alive!!!!!')
        print('my name is',self.name)

    def party(self):
        if self.x < 10:
            print ('so far',self.x)
            self.x +=1
            try:
                self.x = self.party()+1
            except:
                pass
            #self.x = self.x + 1
        else:
            print ('so far',self.x)
    
    # destructor
    # now that i'm thinking of this, this would be 
    # a good place to put an autosave feature
    def __del__(self):
        print('i am ded :(')
        print('my name was ',self.name)
        print('i partied',self.x,'timez')


# instantiating an instance of the class as object "an"
an = PartyAnimal()
imal = PartyAnimal('imal')

an.party()

# What does our new class look like?

print(type(an))
#<class '__main__.PartyAnimal'>

print(dir(an))

'''
['__class__', '__delattr__', '__dict__', '__dir__', 
'__doc__', '__eq__', '__format__', '__ge__', 
'__getattribute__', '__gt__', '__hash__', '__init__', 
'__init_subclass__', '__le__', '__lt__', '__module__', 
'__ne__', '__new__', '__reduce__', '__reduce_ex__', 
'__repr__', '__setattr__', '__sizeof__', '__str__', 
'__subclasshook__', '__weakref__', 'party', 'x']
'''

# Inherets a lot from the default object

# getting reassigned also kills our object
an = 6 
print('an reasssinged to ',an,type(an))