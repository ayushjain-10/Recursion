def sum_natural_numbers(N):
    if N == 1:
        return 1
    else:
        return N + sum_natural_numbers(N - 1)
