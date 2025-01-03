import threading
import time


def worker():
    for _ in range(1000000):
        pass


def print_numbers():
    for i in range(1, 6):
        print(f"Number: {i}")


def print_letters():
    for letter in "abcde":
        print(f"Letter: {letter}")


counter = 0


def increment():
    global counter
    for _ in range(1000000):
        counter += 1


# Создаем два потока
start = time.time()
thread1 = threading.Thread(target=increment)
thread2 = threading.Thread(target=increment)

# # Создаем два потока
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Создаем два потока
# thread1 = threading.Thread(target=worker)
# thread2 = threading.Thread(target=worker)

# Запускаем потоки
start1 = time.time()
print(f"Created: {start1 - start}")
thread1.start()
thread2.start()
# Ждем, пока оба потока завершатся
thread1.join()
end1 = time.time()
print(f"thread1: completed: {end1 - start1}")
print(counter)
thread2.join()
end2 = time.time()
print(f"thread2: completed: {end2 - start1}")
print(counter)
print(f"total: {(end2 - start1) + (end1 - start1)}")
start3 = time.time()
increment()
print(counter)
increment()
print(counter)
# print_numbers()
# print_letters()
# # worker()
# worker()
end3 = time.time()
print(f"without: {end3 - start3}")
