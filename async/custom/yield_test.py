import time


def socket(t) -> None:
    time.sleep(t)
    print("connected")


def sample_connection():
    t = 2
    print("starting connection")
    yield "waiting", socket(t)
    print("doing something")
    t = 1
    print("starting new connection")
    yield "waiting", socket(t)
    print("doing new things")


print("started")
a = sample_connection()
next(a)
time.sleep(1)
next(a)
print("end")
