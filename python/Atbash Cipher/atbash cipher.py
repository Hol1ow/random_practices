#The Atbash cipher is an encryption method in 
#which each letter of a word is replaced with 
#its "mirror" letter in the alphabet: A <=> Z; B <=> Y; C <=> X; etc.
#Create a function that takes a string and applies the Atbash cipher to it.

import string
__lowercase = list(string.ascii_lowercase)
__uppercase = list(string.ascii_uppercase)

def atbash(input_str):
    res = ""
    for c in input_str:
        if c in __lowercase:
            res += __lowercase[-__lowercase.index(c)-1]
        elif c in __uppercase:
            res += __uppercase[-__uppercase.index(c)-1]
        else:
            res += c

    return res

print(atbash("apple"))
print(atbash("Hello world!"))
print(atbash("Christmas is the 25th of December"))