hundreds = int(input())
decimals = int(input())
digits = int(input())


def prime_number(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


for hun in range(1, hundreds + 1):
    for dec in range(1, decimals + 1):
        for dig in range(1, digits + 1):
            if (
                    (hun % 2 == 0) and
                    (dig % 2 == 0) and
                    prime_number(dec)
            ):
                print(f"{hun} {dec} {dig}")