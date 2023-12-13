"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*N):
    s=[x**2 for x in N]
    print(s)
power_numbers(1,2,5,7)
"""
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
"""


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def filter_numbers(a,b):
    if b==ODD:
        return(list(filter(lambda x:x % 2!=0,a)))
    elif b==EVEN:
        return(list(filter(lambda x:x % 2==0,a)))
    elif b==PRIME:
        return (list(filter(is_prime,a)))

a=[1,2,3,4,5,6,7]
print(filter_numbers(a,PRIME))

"""
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
"""
