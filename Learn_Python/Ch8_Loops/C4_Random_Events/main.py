def is_prime(number):
    if number > 1:
        for i in range(2, number+1):
            result = number % i
            print(f"{result} {i}")
