class AA:
        def __init__(self,a,b):
            self.x=a
            self.y=b
        def add(self):
            print(self.x+self.y)
class BB(AA):
        def sub(self):
            print(self.x-self.y)

ob=BB(10,20)
ob1=BB(20,30)
ob.add()
ob1.add()
ob.sub()
ob1.sub()
ob2=AA(1,2)
ob2.add()
ob2.sub()


    