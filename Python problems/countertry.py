import re


def count_vowels_consonants(sentence):
    sentence = re.sub(r'[^a-zA-Z0-9]', '', sentence)
    vowels = 'aeiouAEIOU'
    vowel_count = 0     
    consonant_count = 0
    for char in sentence:
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
    return f'Vowels:{vowel_count} & Consonants:{consonant_count}'

print(count_vowels_consonants("Hello World! Python is awesome."))


    