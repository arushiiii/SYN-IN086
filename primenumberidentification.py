def is_prime(num):
    if num <= 1:
        return False  # 0 and 1 are not prime numbers
    if num == 2:
        return True  # 2 is the only even prime number
    if num % 2 == 0:
        return False  # other even numbers are not prime

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False  # found a divisor, so it's not prime
    return True  # no divisors found, so it's prime

def main():
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")

if __name__ == "__main__":
    main()
