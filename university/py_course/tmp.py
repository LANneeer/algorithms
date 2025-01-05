def exchange(wallet, item):
    exchange_rate = wallet - item
    for i in [50, 20, 10, 5, 2, 1]:
        print(f"{i}: {exchange_rate // i}")
        exchange_rate -= (exchange_rate // i) * i


exchange(100, 45)


ex = lambda rate: [
    "{}: {} {}".format(i, rate // i, rate := rate % i)[:5].strip()
    for i in [50, 20, 10, 5, 2, 1]
]


print(ex(65))
