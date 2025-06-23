# method resolution order // multiple inheritance

class A:
    def show(self):
        print("ini adalah show A")

class B:
     def show(self):
        print("ini adalah show B")


#class C(B,A):
class C(A,B):
    # def show(self):
    #     print("ini adalah show C")
    pass

objek = C()
objek.show()
# help(objek)