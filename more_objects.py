from objects import PartyAnimal as pa 

class PartyDog(pa):
    # attributes
    noise='Arf'

    # methods
    def bark(self):
        print('woof, im a cool party dog')
        print(self.noise)
        print('my name is',self.name)

    def party_down(self):
        self.x -= 1

spot = PartyDog("spot")
print(type(spot))
print(dir(spot))

spot.bark()
spot.party()
spot.party_down()