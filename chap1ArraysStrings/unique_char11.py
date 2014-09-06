"""
Page 73
Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
ans: pg 172
"""

def is_all_unique(string):
    """
    determine if a string has all unique chars
    """
    
    # create a dict to detect, a list will also do  
    char_list = {}

    for char in string:
        if char in char_list:
            return False
        char_list[char] = 1
    
    return True

# test case
assert is_all_unique("hehe") == False
assert is_all_unique("he") == True
assert is_all_unique("testpass") == False

print "Test passed"
