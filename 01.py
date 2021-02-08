def find_sum_of_multiples(n):
    multiples = [num for num in range(n) if num % 3 == 0 or num % 5 == 0]
    return sum(multiples)

print(find_sum_of_multiples(1000))
