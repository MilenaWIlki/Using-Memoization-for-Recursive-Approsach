def factorial_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    else:
        memo[n] = n * factorial_memoization(n - 1, memo)
        return memo[n]

# Example usage:
number = 5
fact = factorial_memoization(number)
print("Factorial of", number, "is", fact)
