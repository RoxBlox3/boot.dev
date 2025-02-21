def is_prime(number):
    if number > 1:
        for i in range(2, (number+2)//2):
            result = number % i
            print(f"{result} {i}")
            if result == 0:
                print(f"{number} is not a prime number.")
                return False
                break
        else:
            print(f"Return loop number {number} result") 
            return True
    else:
        return False
