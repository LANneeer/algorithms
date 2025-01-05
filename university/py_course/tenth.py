numbers = [4, -5, 3, -2, 0, 10, -4, 7, 1]
print("all positive odd", [num for num in numbers if num > 0 and num % 2 != 0])
print("modulo", [abs(num) for num in numbers])
print(
    "count of positive odd", len([num for num in numbers if num > 0 and num % 2 != 0])
)
print("avg", sum(numbers) // len(numbers))
positives = [num for num in numbers if num > 0]
negatives = [num for num in numbers if num < 0]
avg_positive = sum(positives) // len(positives) if positives else 0
avg_negative = sum(negatives) // len(negatives) if negatives else 0
print("avg_negative", avg_negative)
print("avg_positive", avg_positive)
print([num if num >= 0 else 0 for num in numbers])
n = 10
print("sum of range", sum(range(1, n + 1)))
fib_sequence = [1, 1]
[fib_sequence.append(fib_sequence[-1] + fib_sequence[-2]) for _ in range(2, 12)]
print("fibonacci", fib_sequence)
