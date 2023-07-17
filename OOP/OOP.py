class ParentClass1():
    pass

class ParentClass2():
    pass

class SomeStaticClass(ParentClass1, ParentClass2):
    # в скобках после имени класса перечислены классы-родители
    # внутри перечислены поля и методы класса SomeClass
    attr1 = 42
    attr2 = "Yep" # аттрибуты класса
    def method(self, x):
        # код метода, где self - общепринятое имя для ссылки на объект, 
        # в контексте которого вызывается метод
        return 2*x
    
obj = SomeStaticClass() # Экземпляр класса
obj.method(6) # 12
obj.attr1 # 42

class Point(object):
    def __init__(self, x, y, z):
        self.coord = (x, y, z)

p = Point(13, 14, 15)
p.coord # 13, 14, 15

# Динамическое изменение класса

class Something(object):
    pass # плейсхолдер
def squareMethod(self, x):
    return x*x

Something.square = squareMethod # Классы могут динамически изменятся после определения. 
obj = Something()
obj.square(5) # 25

# Статический класс

class SomeStaticClass(object):
    @staticmethod # Декоратор для создания статических методов. 
    # Доступ к таким методам можно получить как из экземпляра класса, так и из самого  класса
    def hello():
        print("Hello, world")

SomeStaticClass.hello() # Hello, world
obj = SomeStaticClass()
obj.hello() # Hello, world