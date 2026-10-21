class my_class:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_name(self):
        print("Rajesh Patel", self.a)

    def get_product(self):      
        print("car , bike , bicycle", self.b)


class demo(my_class):
    def __init__(self, a, b):
        self.a = a
        self.b = b


d = demo("xyz", 150)
d.get_product()
