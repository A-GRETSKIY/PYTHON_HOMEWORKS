def arithmetic_progression(a_0, dx, n):
    return a_0 + n * dx


def geom_progression(b_0, q, n):
    return b_0 * q ** (n - 1)


def get_next_item(start: int | float, step: int | float, n: int, func_tool):
    i = 0
    items = (func_tool(start, step, i) for i in range(n))
    while i < n:
        try:
            yield next(items)
        except:
            break


print(*get_next_item(10, 3, 20, arithmetic_progression))
print(*get_next_item(1, 2, 20, geom_progression))