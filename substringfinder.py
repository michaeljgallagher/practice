'''
Suppose you have an array of strings 'src' and a string 'key':

src = ["minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"]
key = "craft"

Now return all the strings from the 'src' array that contains the key as
substring in them. For example, for above case, the solution should be:

result = ["minecraftgame", innercrafttalent", "stonecrafter"]

Because all the result starings have key i.e. "craft" in them as substring
'''

def stringfinder(src, key):
    res = []
    if len(key) == 0:
        return res
    for i in range(len(src)):
        if len(src[i].split(key)) > 1:
            res.append(src[i])
    return res

src = ["craft", "minecraftgame", "intelligent", "innercrafttalent", "knife", "scissor", "stonecrafter"]
key = "craft"
print(stringfinder(src, key))
