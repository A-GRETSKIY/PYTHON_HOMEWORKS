import timeit


def fibonacci():
    numbers = [0, 1]

    def get_number(n):
        if n < len(numbers):
            return numbers[n]

        curr_item, next_item = numbers[-2], numbers[-1]
        i = len(numbers)

        while i <= n:
            curr_item, next_item = next_item, curr_item + next_item
            numbers.append(next_item)
            i += 1
        return next_item

    return get_number


x = fibonacci()
print(timeit.timeit('x(10)', number=5, setup='from __main__ import x'))