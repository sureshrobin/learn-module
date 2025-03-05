from collections import Counter
def most_frequent(numbers):
    counted = Counter(numbers)
    most = counted.most_common(1)[0][0]
    return most
# Test Case
print(most_frequent([1, 3, 2, 3, 4, 1, 3, 2, 4, 4, 4]))


