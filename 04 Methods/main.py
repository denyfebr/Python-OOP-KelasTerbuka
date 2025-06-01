class Hero:
    #class variable
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    # void function, method tanpa return dan tanpa argument
    def siapa(self):
        print(f"Namaku adalah {self.name}")

    # method dengan argument, tanpa return
    def healthUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health

hero1 = Hero("Sniper", 100, 10, 4)
hero2 = Hero("Mario Bros", 90, 5, 10)

hero1.siapa()
hero1.healthUp(10)
print(hero1.getHealth())


