"""from collections import Counter
def first_non_repeating(s):
    counted = Counter(s)
    dict1 = dict(counted)
    for key,value in dict.items():
        if value ==1:
            print(f'{key} is not repeated')
    return None
    

# Test Cases
print(first_non_repeating("aabbcdd"))
print(first_non_repeating("aabbcc"))"""
from collections import Counter
s = 'aabbcdd'

counted = Counter(s)
print(counted[char])