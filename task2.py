def solve_equation(a: int, b: int, c: int, d: int, x: int) -> bool:
    return a * x ** 3 + b * x ** 2 + c * x + d == 0


a, b, c, d = map(int, input().split())

roots = list()
for x in range(-100, 100 + 1):
    if solve_equation(a, b, c, d, x):
        roots.append(x)

print(*roots)
