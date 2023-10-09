import math


# def func(x):
#     return math.sqrt(math.e ** x - 1)

def func(x):
    return math.e ** (x + math.cos(x))

# values = [
#     0,
#     0.1,
#     0.2,
#     0.3,
#     0.4,
#     0.5,
#     0.6,
#     0.7,
#     0.8,
#     0.9,
#     1
# ]


values = [
    -1,
    -0.5,
    0,
    0.5,
    1,
    1.5,
    2
]

deltaX = 0.5


# SHOULD NOT NEED TO BE MESSED WITH

sum = 0
for (i, value) in enumerate(values):
    if i == 0 or i == len(values) - 1:
        sum += func(value)
        continue

    sum += 2 * func(value)

sum *= deltaX / 2

print(f"Trapezoidal: {sum}")

sum = 0
for (i, value) in enumerate(values):
    pattern = 2 if i % 2 == 0 else 4
    result = func(value)
    if i == 0 or i == len(values) - 1:
        sum += result
    else:
        sum += pattern * result

sum *= deltaX / 3

print(f"Simpsons: {sum}")
