def common_characters(str1, str2):
    # Your code here
    set1 = set(str1.lower())
    set2 = set(str2.lower())
    common = set1 & set2
    joined = " ".join(common)
    return joined

# Test Case
print(common_characters("Hello World!", "Python World!"))
