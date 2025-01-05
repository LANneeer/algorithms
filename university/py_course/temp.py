class MyTime:
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds


class ChildTime(MyTime):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pm = False
        self.update_analog()

    def update_analog(self):
        if self.hours > 11:
            self.hours -= 12
            self.pm = True

    def show(self):
        print(
            f"{self.hours if self.hours > 10 else '0' + str(self.hours)}:"
            f"{self.minutes if self.minutes > 10 else '0' + str(self.minutes)}:"
            f"{self.seconds if self.seconds > 10 else '0' + str(self.seconds)} "
            f"{'p.m.' if self.pm else 'a.m.'}"
        )


time = ChildTime(13, 0, 0)
time.show()
