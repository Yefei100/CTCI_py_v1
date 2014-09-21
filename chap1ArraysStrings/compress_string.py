"""
Page 73

Implemented a method to perform basic string compression using the counts of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become smaller than the original string, your method should return the original string.

ans: pg 176
"""

def compress_string(string):
    
    char_counters = []
    ref = string[0]
    counter = 1
    length = len(string)

    for idx in range(1, length):
        if string[idx] == ref:
            counter += 1
	else:
	    char_counters.append((ref, counter))
	    ref = string[idx]
	    counter = 1
    
    char_counters.append((ref, counter))

    for char_counter in char_counters:
        if char_counter[1] != 1:
	    output_string = ""
	    for char_counter in char_counters:
	        output_string += char_counter[0] + str(char_counter[1])
	    return output_string

    return string

print compress_string("aabcccccaaa")
print compress_string("abcdabcd")
