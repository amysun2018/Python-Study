class MyClass:
    """A simple example class"""

    i = 12345  # this is class attribute
    print(globals())

    def f_print(self):
        return 'hello world'


# in python3 this is equivalent to 'class Myclass2(object):'
class Myclass2(object):
    pass


if __name__ == '__main__':
    print(MyClass.i)
    my_ojject = MyClass()
    my_ojject.f_print()
    print(my_ojject.i)
    my_ojject = Myclass2()
