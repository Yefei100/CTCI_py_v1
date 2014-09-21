"""
Page 74

Assume you have a method is_substring that checks if one word is a substring of another. Given 2 strings, s1 and s2, write code to check if s2 is a rotation of s1, using only on call to is_substring(e.g. "waterbottle is a rotation of "erbottlewat").

ans: pg 182
"""

def is_rotation(string1, string2):
    concatenate_string = string1 + string2
    return is_substring(string1, concatenate_string)


