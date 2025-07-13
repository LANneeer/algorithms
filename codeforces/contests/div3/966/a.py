def is_primary(num: int) -> str:
    num = str(num)
    if len(num) >= 3 and num[:2] == "10" and num[2] != "0" and int(num[2:]) >= 2:
        return "YES"
    else:
        return "NO"


def primary_number(t: int) -> str:
    while t != 0:
        print(is_primary(int(input())))
        t -= 1


primary_number(int(input()))
