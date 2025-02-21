x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

if x < x1:
    x_closest = x1
elif x > x2:
    x_closest = x2
else:
    x_closest = x

if y < y1:
    y_closest = y1
elif y > y2:
    y_closest = y2
else:
    y_closest = y

if x_closest == x1 and y_closest == y1:
    print("SW")
elif x_closest == x1 and y_closest == y2:
    print("NW")
elif x_closest == x2 and y_closest == y1:
    print("SE")
elif x_closest == x2 and y_closest == y2:
    print("NE")
elif x_closest == x1:
    print("W")
elif x_closest == x2:
    print("E")
elif y_closest == y1:
    print("S")
elif y_closest == y2:
    print("N")
else:
    print("on float")
