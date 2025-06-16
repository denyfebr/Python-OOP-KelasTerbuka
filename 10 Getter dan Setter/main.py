class Hero:
    
    def __init__(self,name,health,armor):
        # self.__name = name
        self.name = name
        self.__health = health
        self.__armor = armor
        # self.info = "name {} : \n\thealth: {}".format(self.__name,self.__health)

    @property
    def info(self):
        return "name {} : \n\thealth: {}".format(self.name,self.__health)
    
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input

    @armor.deleter
    def armor(self):
        self.__armor = None

    
print('merubah info')
sniper = Hero('sniper',100,10)
print(sniper.info)
sniper.name = 'dadang'
print(sniper.info)
print('='*20)
print('getter dan setter untuk __armor')
print(sniper.armor)
# sniper.armor = 10 Error = berhasil!! Enkapsulasi jalan
sniper.armor = 50 # berhasil karena sdh ada setter nya
print(sniper.armor)
print('='*20)
print('delete armor')
print(sniper.__dict__)
del sniper.armor
print(sniper.__dict__)