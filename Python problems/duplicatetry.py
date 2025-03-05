from collections import Counter
def find_duplicates(numbers):
    duplicate_count = (Counter(numbers))
    duplicate_list = []
    for value in duplicate_count:
        if value > 1:
            duplicate_list = duplicate_list.append(value)
        else:
            pass
        return duplicate_list

    

# Test Case
print(find_duplicates([1, 2, 3, 4, 5, 2, 6, 7, 3, 8, 9, 1]))
