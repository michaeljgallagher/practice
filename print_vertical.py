'''
Given a string s. Return all the words vertically in the same order in which
they appear in s.
Words are returned as a list of strings, complete with spaces when is
necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be
only one word.

Constraints:

    1 <= s.length <= 200
    s contains only upper case English letters.
    It's guaranteed that there is only one space between 2 words.
'''

def print_vertical(s):
    words = s.split()
    max_length = 0
    for word in words:
            max_length = max(max_length, len(word))
    vert = [''] * max_length
    for word in words:
        for i in range(max_length):
            if i < len(word):
                vert[i] += word[i]
            else:
                vert[i] += ' '
    return [x.rstrip() for x in vert]


print(print_vertical("HOW ARE YOU") == ["HAY","ORO","WEU"])
print(print_vertical("TO BE OR NOT TO BE") == ["TBONTB","OEROOE","   T"])
print(print_vertical("CONTEST IS COMING") == ["CIC","OSO","N M","T I","E N","S G","T"])

