# 1
def sum_to(n):
    return sum(range(1, n + 1))


# 2
def largest(numbers):
    largest = 0
    for number in numbers:
        if number > largest:
            largest = number
            return largest


# 3
def occurrences(string, substr):
    count = 0
    start = 0
    while True:
        index = string.find(substr, start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count


# 4
def product(*args):
    product = 1
    for arg in args:
        product *= arg
    return product
