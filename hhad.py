class AA:
        def __init__(self, a,b):
            self.x=a
            self.y=b
        def add(self):
            print(self.x+self.y)
class BB:
         def __init__(self, a,b):
             self.x=a
             self.y=b
         def sub(self):
             print(self.x-self.y)
class CC:
         def __init__(self, a,b):
             self.x=a
             self.y=b
         def mul(self):
            print(self.x*self.y)
class DD:
        def __init__(self, a,b):
            self.x=a
            self.y=b
        def div(self):
            print(self.x%self.y)
ob=AA(10,20)
ob.add()
ob=BB(10,20)
ob.sub()
ob=CC(10,20)
ob.mul()
ob=DD(10,20)
ob.div()

            
             
             
    