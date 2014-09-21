"""
Page 73
Write a mehtod to replace all spaces in a string with '%20'.

Example:
  "Mr John Smith       "

ans: pg 175
"""

def replace_spaces(string1):
    
    words = string1.strip().split()
    new_string = ""
    last_word = words.pop()

    for char in words:
        new_string = new_string + char + "%20"
	
    new_string += last_word
    return new_string, string1

print replace_spaces("Mr Jhon Smith    ")





