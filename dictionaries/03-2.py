# Exercise 3: Medium
# Write a program that counts the frequency of each character in a given string and stores the results in a dictionary.
# Ignore white space and punctuation marks. Print the dictionary.
#
#

letters = 0
others = 0
string = {}

text = input("\nType a sentence: ").lower()

for i in text:
    if not i in string and (ord(i) > 96 and ord(i) < 123): 
        string[i] = 1
        letters += 1
    elif i in string:
        string[i] += 1
        letters += 1
    else:
        others += 1

for i in string:
    if string[i] > 0:
        print(f' {i} = {string[i]}')

print(f"\nThere are {letters+others} characteres being  {letters} letters, {others} symbols or numbers.\n")

