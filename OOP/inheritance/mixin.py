# Mixins Example
class A:
    def method_a(self):
        return "A method"


class B:
    def method_a(self):
        return "B method"


def mixin(classes: list[object]) -> object:
    class C:
        pass

    print(classes)
    for cls in classes:
        for attr in dir(cls):
            if not attr.startswith("__"):
                setattr(C, attr, getattr(cls, attr))
    return C


class MixinC(mixin([A, B])):
    def method_c(self):
        return "C method"


print(MixinC().method_a())
