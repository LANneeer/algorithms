from OOP.inheritance.composition import CompositionC
from OOP.inheritance.mixin import MixinC
from OOP.inheritance.prototype import CPrototype
from OOP.inheritance.traits import TraitsC

mixin_instance = MixinC()
traits_instance = TraitsC()
prototype_instance = CPrototype()
composition_instance = CompositionC()

# Testing and showcasing
test_cases = [
    mixin_instance.method_a(),
    mixin_instance.method_b(),
    mixin_instance.method_c(),
    traits_instance.method_a(),
    traits_instance.method_b(),
    traits_instance.method_c(),
    prototype_instance.method_a(),
    prototype_instance.method_b(),
    prototype_instance.method_c(),
    composition_instance.method_c(),
]

test_cases
