# Composition Example
class AComposition:
    def method_a(self):
        return "A composition method"


class BComposition:
    def method_b(self):
        return "B composition method"


class CompositionC:
    def __init__(self):
        self.a = AComposition()
        self.b = BComposition()

    def method_c(self):
        return "C composition method", self.a.method_a(), self.b.method_b()


print(CompositionC().method_c())
