'''from collections import Counter
def first_non_repeating(s):
    counted = Counter(s)
    return type(counted)
    

# Test Cases
print(first_non_repeating("aabbcdd"))
print(first_non_repeating("aabbcc"))'''

from collections import Counter

s = "aabbdd"
s1 = list(s)
counted = dict(Counter(s1))

for key,value in counted.items():
return None







