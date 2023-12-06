def extended_gcd(a, b):
    # Initialize coefficients
    s0: int = 1
    s1: int = 0
    t0: int = 0
    t1: int = 1

    while b > 0:
        # Calculate quotient and remainder
        q = int(a / b)
        r = a % b

        # Update coefficients
        s0_temp = s0
        s0 = s1
        s1 = s0_temp - q * s1

        t0_temp = t0
        t0 = t1
        t1 = t0_temp - q * t1

        # Update a and b
        a = b
        b = r

    # The coefficients s0 and t0 are the Bézout coefficients
    # The gcd is the last non-zero remainder (a)
    return [a, [s0, t0]]


def main():
    tests = [
        [252, 356],
        [144, 89],
        [1001, 100001]
    ]

    for (a, b) in tests:
        result = extended_gcd(a, b)
        print(f"gcd({a}, {b}) = {result[0]}")
        print(f"Bezout coefficients: {result[1]}\n")


if __name__ == "__main__":
    main()
