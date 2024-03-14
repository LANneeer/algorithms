# Traits Example
class TraitA:
    def method_a(self):
        return "Trait A method"


class TraitB:
    def method_b(self):
        return "Trait B method"


def trait(A: object, B: object) -> object:
    class C:
        pass

    for attr in dir(A):
        if not attr.startswith("__"):
            setattr(C, attr, getattr(A, attr))
    for attr in dir(B):
        if not attr.startswith("__"):
            if not hasattr(C, attr):
                setattr(C, attr, getattr(B, attr))
            else:
                raise AttributeError(f"Attribute {attr} already exists in C")
    return C


class TraitsC(trait(TraitA, TraitB)):
    def method_c(self):
        return "Trait C method"


print(TraitsC().method_z())
