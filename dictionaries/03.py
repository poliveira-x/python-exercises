# Exercise 3: Medium
# Write a program that counts the frequency of each character in a given string and stores the results in a dictionary.
# Ignore white space and punctuation marks. Print the dictionary.
#

letters = 0
others = 0
string = {}
for i in range(97, 123):
    string[chr(i)] = 0 

text = input("\nType a sentence: ").lower()

for i in text:
    if ord(i) < 97 or ord(i) > 122:
        others += 1
        pass
    else:
        string[i] = string[i] + 1
        letters += 1

for i in string:
    if string[i] > 0:
        print(f' {i} = {string[i]}')

print(f"\nThere are {letters+others} characteres being  {letters} letters, {others} symbols or numbers.\n")

