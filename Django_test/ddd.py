"""
通过 new 函数实现简单的单例模式。
"""
class Book:
    def __new__(cls, title):
        if not hasattr(cls, "_ins"):
            cls._ins = super().__new__(cls)
        print('in __new__')
        return cls._ins

    def __init__(self, title):
        print('in __init__')
        #super().__init__()
        self.title = title


if __name__ == '__main__':
    b = Book('The Spider Book')
    b2 = Book('The Flask Book')
    print(id(b))
    print(id(b2))
    print(b.title)
    print(b2.title)
    ######