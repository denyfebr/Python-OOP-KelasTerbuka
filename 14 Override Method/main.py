class Hero:

    def __init__(self,name,health):
        self.name = name
        self.health = health

    # def showInfo(self,tipe):
    #     print("{} \n\tTipe:{},\n\thealth: {}".format(self.name,tipe,self.health))

    def showInfo(self):
        print("ini adalah showInfo di class Hero")
        print("{} health: {}".format(
            self.name,
            self.health)
        )

class Hero_intelligent(Hero):
    
    def __init__(self, name):
        super().__init__(name,100)

    #override
    def showInfo(self):
        print("ini adalah showInfo di subclass Hero_intelligent")
        print("{} \n\ttipe: intelligent,\n\thealth: {}".format(
                self.name,
                self.health
            )
        )

class Hero_strength(Hero):
    def __init__(self, name):
        super().__init__(name,200)

lina = Hero_intelligent('lina')
axe = Hero_strength('axe')

lina.showInfo()
print('\n')
axe.showInfo()