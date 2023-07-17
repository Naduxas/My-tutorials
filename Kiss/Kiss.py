import inspect # требуется для метода inspect 

class Shape:
    def find_intersection(self, shape):
        method = MethodFinder.find(type(self), "find_intersection", type(shape))

        if method is not None:
            return method(self, shape)

        return shape.find_intersection(self)


class Circle(Shape):
    @staticmethod
    def find_intersection(rectangle):
        return RoundedRectangle()  # Здесь также может быть возвращен Rectangle или Circle, в зависимости от их размеров. Но для простоты будем считать, что метод всегда возвращает RoundedRectangle.


class Rectangle(Shape):
    @staticmethod
    def find_intersection(rounded_rectangle):
        return Rectangle()


class RoundedRectangle(Shape):
    pass


class MethodFinder:
    @staticmethod
    def find(class_type, function_name, parameter_type):
        methods = inspect.getmembers(class_type, predicate=inspect.ismethod) # возвращаем все, что есть в объекте

        for method_name, method in methods:
            if method_name == function_name and len(inspect.signature(method).parameters) == 2 and isinstance(inspect.signature(method).parameters['shape'].annotation, parameter_type):
                return method


if __name__ == "__main__":
    shape = Rectangle()
    shape_intersection = shape.find_intersection(Circle())
    print(type(shape_intersection))
