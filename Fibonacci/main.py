"""
The Fibonacci sequence is a series of numbers in which each number
is the sum of the two preceding ones, starting from 0 and 1.

Formally:
F(0) = 0
F(1) = 1
F(n) = F(n - 1) + F(n - 2) for n >= 2

In Python, the Fibonacci sequence can be generated using iterative
or recursive approaches.

The recursive version is simple but inefficient due to repeated
calculations, while the iterative version is more efficient
and commonly preferred.

Time complexity:
- Recursive version: O(2^n)
- Iterative version: O(n)

Space complexity:
- Recursive version: O(n) due to recursion stack
- Iterative version: O(1)
"""


from datetime import datetime


def time_it(func):
    def wrapper(*args, **kwargs):
        if not getattr(wrapper, '_running', False):
            wrapper._running = True
            start = datetime.now()
            result = func(*args, **kwargs)
            end = datetime.now()
            print(f"{func.__name__} processing time: {end - start}")
            wrapper._running = False
            return result
        else:
            return func(*args, **kwargs)
    wrapper._running = False
    return wrapper


@time_it
def fib_recursive(n: int) -> int | list[int]:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2)


@time_it
def fib_fast(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    current = 1

    for i in range(2, n+1):
        prev, current = current, current + prev

    return current


### !!! ATTENTION !!! Recursive fib is going to take long if you choose fib_number=35 or more
def main() -> None:
    fib_nuber = 30
    print(f"Fib fast result: {fib_fast(fib_nuber)}")
    print(f"Fib recursive result: {fib_recursive(fib_nuber)}")


if __name__ == '__main__':
    main()
