# divisible by three print fizz
# divisible by 5 print buzz
# divisible by both print fizzbuzz
def divisible(n):
    for n in range(1, n):
        if (n % 3 == 0) and (n % 5 == 0):
            print("Fizzbuzz")
        elif n % 5 == 0:
            print("Buzz")
        elif n % 3 == 0:
            print("Fizz")
        else:
            print(n)
