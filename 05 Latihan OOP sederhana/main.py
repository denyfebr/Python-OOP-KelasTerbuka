class Hero:
    #class variable
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

    def menyerang(self,lawan):
        print(f"{self.name} menyerang {lawan.name}")
        lawan.diserang(self, self.power)

    def diserang(self,lawan, power_lawan):
        print(f"{self.name} diserang {lawan.name}")
        attack_received = power_lawan/self.armor
        print(f"attack impact : {str(attack_received)}")
        self.health -= attack_received
        print(f"health {self.name} tersisa {str(self.health)}")
      

sniper = Hero("Sniper", 100, 10, 5)
rikimaru = Hero("Rikimaru", 100, 20, 10)

sniper.menyerang(rikimaru)
print("\n")
rikimaru.menyerang(sniper)
print("\n")
rikimaru.menyerang(sniper)




