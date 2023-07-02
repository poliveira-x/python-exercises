# Exercise 2: Easy
# Write a program that takes a dictionary containing the names and ages of five people as input.
# The program should find the person with the maximum age and print their name.
#

clients = {
        "peter" : 25,
        "megan" : 52,
        "johsua": 48,
        "Kate" : 21,
        "Mary": 29,
}


def find_older(people):
    name = ''
    age = 0

    for i in people:
        if people[i] > age:
            age =people[i]
            name = i

    return name


print(f"\n\n{clients}\n\n{find_older(clients)}\n\n")


