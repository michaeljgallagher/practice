'''
Given a list of words, each word can be written as a concatenation of the
Morse code of each letter. For example, "cba" can be written as "-.-..--...",
(which is the concatenation "-.-." + "-..." + ".-").
We'll call such a concatenation, the transformation of a word.

Return the number of different transformations among all words we have.

Example:
Input: words = ["gin", "zen", "gig", "msg"]
Output: 2
Explanation: 
The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."

There are 2 different transformations, "--...-." and "--...--.".
'''

import string

morse = [".-","-...","-.-.","-..",".","..-.","--.",
             "....","..",".---","-.-",".-..","--","-.",
             "---",".--.","--.-",".-.","...","-","..-",
             "...-",".--","-..-","-.--","--.."]
letters = list(string.ascii_lowercase)
mmap = {letters[i]:morse[i] for i in range(len(morse))}

def convert(s):
    t = ''
    for c in s:
        t += mmap[c]
    return t

def uniqueMorseRepresentations(words):
    transformations = []
    for word in words:
        transformations.append(convert(word))   
    return len(set(transformations))

words = ["gin", "zen", "gig", "msg"]
print(uniqueMorseRepresentations(words)) # 2
