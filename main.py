from random import randint


def gen_array(length: int, min_: int = 0, max_: int = 100) -> list:
    return [randint(min_, max_) for _ in range(length)]


if __name__ == '__main__':
    array = gen_array(100)
    # TODO: create visualization of different algorithms
