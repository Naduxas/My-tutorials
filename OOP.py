class SomeClass(ParentClass1, ParentClass2):
    # поля и методы класса SomeClass
    attr1 = 42
    attr2 = "Yep" # аттрибуты класса
    def method(self, x):
        # код метода, где self - общепринятое имя для ссылки на объект, 
        # в контексте которого вызывается метод
        return 2*x
    
obj = SomeClass() # Экземпляр класса
obj.method(6) # 12
obj.attr1 # 42

class Point(object):
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

p = Point(13, 14, 15)
p.coord # 13, 14, 15

class Something(object):
    pass # плейсхолдер
def squareMethod(self, x):
    return x*x

Something.square = squareMethod
obj = Something()
obj.square(5) # 25
