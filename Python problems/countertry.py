import re

def count_vowels_consonants(sentence):
    # Remove all non-alphabetic characters (punctuation and spaces)
    sentence = re.sub(r'[^a-zA-Z]', '', sentence)
    
    # Initialize counters for vowels and consonants
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in sentence:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    
    return f"Vowels: {vowel_count}, Consonants: {consonant_count}"

# Test Case
print(count_vowels_consonants("Hello World! Python is awesome."))
