# u can write any number of functions in this py file


def add(a,b):
    return a+b

def sub(a,b):
    return a-b


class mathOperations:

    def __init__(self,a,b,):
        self.a = a
        self.b = b


    def ADD(self):
        return self.a + self.b
    
class otherClass(mathOperations):

    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def SUB(self):
        return self.a - self.b, self.c
    
