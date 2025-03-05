numbers = [1, 2, 4, 6, 3, 7, 8]
n = 8

set1 = set(numbers)
length = len(set1)
total_sum = n * (n+1) // 2
actual_sum = sum(set1)
missing = total_sum - actual_sum
print(missing)