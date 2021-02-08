def find_sum_of_multips(x):
    multips = [num for num in range(x) if num % 3 == 0 or num % 5 == 0]
    return sum(multips)
