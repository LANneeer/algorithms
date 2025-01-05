class MyTime:
    def __init__(self, total_seconds):
        self.second = total_seconds
        self.hour = 0
        self.minute = 0
        self.define_time_by_seconds()

    def define_time_by_seconds(self):
        self.hour = self.second // 3600
        remaining_seconds = self.second % 3600
        self.minute = remaining_seconds // 60
        self.second = remaining_seconds % 60

    def show_time(self):
        print(
            f"Time is {self.hour} hours, {self.minute} minutes, {self.second} seconds."
        )


class MyListClass:
    def __init__(self, int_list):
        self.int_list = int_list

    def get_max_min(self):
        max_value = self.int_list[0]
        min_value = self.int_list[0]
        for num in self.int_list[1:]:
            if num > max_value:
                max_value = num
            if num < min_value:
                min_value = num
        return max_value, min_value

    def get_duplicates_list(self):
        counts = {}
        duplicates = []
        for num in self.int_list:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num in counts:
            if counts[num] > 1:
                duplicates.append(num)
        return duplicates

    def get_duplicates_dict(self):
        counts = {}
        duplicates = {}
        for num in self.int_list:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        for num in counts:
            if counts[num] > 1:
                duplicates[num] = counts[num]
        return duplicates

    def get_sum(self):
        total = 0
        for num in self.int_list:
            total += num
        return total


if __name__ == "__main__":
    total_seconds = int(input("Write seconds: "))
    time_instance = MyTime(total_seconds)
    time_instance.show_time()

    numbers = [int(x) for x in input("Write list: ").split()]
    my_list = MyListClass(numbers)

    max_value, min_value = my_list.get_max_min()
    print("Max:", max_value)
    print("Min:", min_value)
    print("Duplicates:", my_list.get_duplicates_list())
    print("Counts:", my_list.get_duplicates_dict())
    print("Sum:", my_list.get_sum())
