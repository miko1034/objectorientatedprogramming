class Animal():
    def __init__(self, animalspecies = "unknown",age=0,threatlevel="peaceful",hungerlevel=0):
        self.animalspecies = animalspecies
        self.age= age
        self.threatlevel = threatlevel
        self.hungerlevel = hungerlevel
    def setspecies(self,speciesname):
        self.animalspecies = speciesname
    def setage(self,inp_age):
        self.age = inp_age
    def sethungerlevel(self,inp_hunger):
        if inp_hunger > 0:
            if inp_hunger < 11:
                self.hungerlevel = inp_hunger
    def changethreatlevel(self):
        if self.hungerlevel <= 3:
            self.threatlevel = "peaceful"
        elif self.hungerlevel > 3:
            if self.hungerlevel < 8:
                self.threatlevel = "narky"
        elif self.hungerlevel <=  8:
            self.threatlevel = "agressive"

cat = Animal()
cat.setspecies("Cat")
cat.setage(5)
cat.sethungerlevel(7)
cat.changethreatlevel()
print("done")