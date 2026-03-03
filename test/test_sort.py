import time
from statistics import mean

from helpers.mock_data import gen_array
from sort import bubble_sort, insertion_sort, merge_sort, quick_sort, selection_sort, heap_sort

def test_bubble_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert bubble_sort(array) == sorted_array, bubble_sort(array)


def test_insertion_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert insertion_sort(array) == sorted_array, insertion_sort(array)


def test_selection_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert selection_sort(array) == sorted_array, selection_sort(array)


def test_heap_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert heap_sort(array) == sorted_array, heap_sort(array)


def test_merge_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert merge_sort(array) == sorted_array, merge_sort(array)


def test_quick_sort():
    array = gen_array(length=100)
    sorted_array = sorted(array)
    assert quick_sort(array) == sorted_array, quick_sort(array)


def _time_once(func, data):
    arr = list(data)
    t0 = time.perf_counter()
    out = func(arr)
    t1 = time.perf_counter()
    # if len(arr) <= 20_000:
    #     assert out == sorted(data)
    return t1 - t0

def time_func(func, data, repeats=5):
    times = [_time_once(func, data) for _ in range(repeats)]
    return min(times), mean(times)

def human(seconds):
    if seconds < 1e-3:
        return f"{seconds*1e6:.1f} µs"
    if seconds < 1:
        return f"{seconds*1e3:.2f} ms"
    return f"{seconds:.3f} s"

def run_speed_tests(sizes=(100, 1_000, 5_000, 10_000), repeats=5):
    algos = [
        ("merge_sort", merge_sort),
        ("quick_sort", quick_sort),
        ("heap_sort", heap_sort),
    ]
    print("\n=== BENCHMARK: скорость сортировок (best/avg из повторов) ===")
    print(f"повторов: {repeats}\n")

    header = f"{'n':>8} | " + " | ".join([f"{name:^24}" for name, _ in algos])
    subhdr = f"{'':>8} | " + " | ".join([f"{'best / avg':^24}" for _ in algos])
    print(header)
    print("-" * len(header))
    print(subhdr)
    print("-" * len(header))

    for n in sizes:
        data = gen_array(length=n)
        row = [f"{n:>8} | "]
        for name, fn in algos:
            best, avg = time_func(fn, data, repeats=repeats)
            row.append(f"{human(best):>10} / {human(avg):<10}")
        print(" | ".join(row))

    print("\nПримечание: входные данные одинаковые для всех алгоритмов одного n; "
          "на каждый прогон берётся свежая копия массива.")

if __name__ == '__main__':
    test_merge_sort()
    # test_quick_sort()
    # test_heap_sort()
    print("Корректность: OK")

    run_speed_tests(
        sizes=(100, ),
        repeats=5
    )
