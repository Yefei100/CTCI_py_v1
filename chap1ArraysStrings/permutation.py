"""
Page 73
Given 2 strings, write a method do decide if one is a permutation of the other
ans: pg 174
"""

def is_permutation(string1, string2):

    # we only count lower case, which is not always true ...
    string1 = string1.lower().strip() 
    string2 = string2.lower().strip()

    char_list1 = {}
    for char in string1:
        if char not in char_list1:
	    char_list1[char] = 1
        else:
	      char_list1[char] += 1

    for char in string2:
        if char not in char_list1:
	    return False
        if char_list1[char] != string2.count(char):
	    return False

    return True

print is_permutation("hehe", "eheh")
print is_permutation("hehe", "hehehe")
print is_permutation("HHHeee", "hehehE")
print is_permutation(" HHHeee", "hehehE   ")
