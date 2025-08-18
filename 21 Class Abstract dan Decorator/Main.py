from abc import ABC, abstractmethod

class Button(ABC):

    @abstractmethod
    def click(self):
        pass


class pushButton(Button):

    def click(self):
        print("push button click")


tombol1 = pushButton()
tombol1.click()