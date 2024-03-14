class A:
    def method_a(self):
        return "A method"


class B(A):
    def method_a(self):
        return "B method"


class C(B):
    def method_a(self):
        return "C method"


class D(C):
    def method_a(self):
        return "D method"


print(C().method_a())
