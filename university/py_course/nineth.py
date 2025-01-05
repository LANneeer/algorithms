class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.seconds = seconds
        self.minutes = minutes
        self.hours = hours

    def time_to_seconds(self):
        return self.hours * 360 + self.minutes * 60 + self.seconds

    def time_to_minutes(self):
        return self.hours * 60 + self.minutes + self.seconds // 60

    def output(self):
        print(f"{self.hours}:{self.minutes}:{self.seconds}")


class ChildTime(MyTime):
    def analog_output(self):
        if self.hours > 11:
            self.hours = self.hours - 12
            pm = True
        else:
            pm = False
        return "{}:{}:{} {}".format(
            self.hours, self.minutes, self.seconds, "p.m." if pm else "a.m."
        )


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Circle(Point):
    def __init__(self, x: int, y: int, radius: float):
        super().__init__(x, y)
        self.radius = radius

    def getArea(self) -> float:
        return 3.14 * (self.radius**2)

    def getCircumference(self) -> float:
        return 2 * 3.14 * self.radius


if __name__ == "__main__":
    time = MyTime(20, 45, 30)
    print("times")
    print(time.time_to_seconds())
    print(time.time_to_minutes())
    child_time = ChildTime(0, 0, 1)
    print(child_time.analog_output())

    circle = Circle(5, 5, 3.5)
    print("circles")
    print(circle.getArea())
    print(circle.getCircumference())
