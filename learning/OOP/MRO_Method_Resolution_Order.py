# === УРОК 44 Udemy_eng. MRO: Method Resolution Order ===

#     A
#   /  \
#  B   C
#  \  /
#   D


class A:
    def someMethod(self):
        print('Method of class A')

    pass


class B(A):
    def someMethod(self):
        print('Method of class B')

    pass


class C(A):
    def someMethod(self):
        print('Method of class C')

    pass


class D(B, C):
    def someMethod(self):
        print('Method of class D')

    pass


# __mro__, mro(), help()  - увидеть древо наследия
print(D.__mro__)
print(D.mro())
help(D)

someObject = D()
someObject.someMethod()
