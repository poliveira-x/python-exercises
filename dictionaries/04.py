# Exercise 4: Medium
# Write a program that takes two dictionaries as input and merges them into a single dictionary.
# If there are common keys, the values should be summed. Print the merged dictionary.
#

fruits1 = {'banana' : 12,
           "orange" : 8,
           "apple" : 3,
           "avocado" : 6,}

fruits2 = {"pear" : 14,
           "apple" : 7,
           "lemon" :6,
           "orange" : 2,}


print(fruits1, fruits2)
print('*'*40)

def make_new_dict(dict1, dict2):
    key = ''
    value = ''
    new_dict = {}
    def extract(dictionary):
        for i in dictionary:
            new_dict[i] = dictionary[i]

        
    extract(dict1)
    extract(dict2)

    print(new_dict)


print(make_new_dict(fruits1, fruits2))




