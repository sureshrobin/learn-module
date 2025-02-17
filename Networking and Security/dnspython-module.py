def is_it_palindrome(s):
    s_inverse = s[::-1]
    if s == s_inverse:
        print(f'{s} is a palindrome')
    else:
        print(f'{s} is not a palindrome')

is_it_palindrome('madam')


