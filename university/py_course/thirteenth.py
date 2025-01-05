def simple_calculator():
    try:
        result = int(input("input value: "))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        result = 0
    while True:
        try:
            operator = input("input operator (+, -, *, /, %, =): ")

            if operator == "+":
                num1 = int(input("input value: "))
                result += num1
            elif operator == "-":
                num1 = int(input("input value: "))
                result -= num1
            elif operator == "*":
                num1 = int(input("input value: "))
                result *= num1
            elif operator == "/":
                num1 = int(input("input value: "))
                result /= num1
            elif operator == "%":
                num1 = int(input("input value: "))
                result %= num1
            elif operator == "=":
                break
            else:
                raise ValueError("Invalid operator!")

        except ValueError as ve:
            print(f"ValueError: {ve}")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except TypeError:
            print("Error: Invalid data type.")
    print(f"Result: {result}")


simple_calculator()
