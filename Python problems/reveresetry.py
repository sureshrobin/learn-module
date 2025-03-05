def reverse_words(sentence):
    word = sentence.split()
    revword = word[::-1]
    joined = " ".join(revword)
    return joined

# Test Case
print(reverse_words("Python is awesome! Let's reverse the words."))

