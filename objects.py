#Sample class

class PartyAnimal:
    x = 0

    def party(self):
        if self.x < 100:
            print ('so far',self.x)
            self.x +=1
            try:
                self.x = self.party()+1
            except:
                pass
            #self.x = self.x + 1
        else:
            print ('so far',self.x)


an = PartyAnimal()

an.party()