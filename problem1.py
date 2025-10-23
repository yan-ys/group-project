#function counts number of vowels in a word not counting y as a vowelgit add problemX.py

def count_vowels(s):
    #word = s
    count = 0
    for letter in s:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
            count += 1
        if letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            count += 1
    return count

print(count_vowels(input('type a word: ')))