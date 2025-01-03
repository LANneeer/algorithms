import concurrent.futures


def worker(data):
    # Здесь происходит обработка данных
    result = data * 2
    return result


data = [1, 2, 3, 4, 5]

# Создаем пул потоков
with concurrent.futures.ThreadPoolExecutor() as executor:
    results = list(executor.map(worker, data))

print("Результаты:", results)
