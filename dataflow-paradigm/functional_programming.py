from typing import List

def filter_even(numbers: List[int]) -> List[int]:
    return list(filter(lambda x: x % 2 == 0, numbers))

def calculate_square(numbers: List[int]) -> List[int]:
    return list(map(lambda x: x ** 2, numbers))

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5, 6]

    even_numbers = filter_even(data)
    squared_numbers = calculate_square(even_numbers)

    print("Squares of even numbers:", squared_numbers)
