# Простой скрипт на Python для подсчета суммы двух чисел

def sum_numbers(a, b):
    return a + b

if __name__ == "__main__":
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = sum_numbers(num1, num2)
    print("Сумма чисел:", result)