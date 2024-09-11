#3.Write a Python function to count the number of vowels and consonants
#in a given string.

#Example:  In the string "Hello", there are 2 vowels ('e', 'o') and
#3 consonants ('H', 'l', 'l').
text =input("Enter a string")
vowels = set('aeiouAEIOU')
vowel_count = 0
consonant_count = 0

for char in text:
# TO Check if the character is a letter or of other data type  
    if char.isalpha():  
        if char in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"Vowels: {vowel_count}, Consonants: {consonant_count}")
# Output: Vowels: 2, Consonants: 3

