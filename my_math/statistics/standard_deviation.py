def stdev(*args) -> int:
    qty = len(args)
    avg = round(sum(args) / qty)
    sigma = 0
    for i in args:
        sigma += (i - avg) ** 2
    return round((sigma / (qty - 1)) ** 0.5)
