'''
If a name has exactly 4 letters in it, keep it. If not, remove it.

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

i.e.

Note: keep the original order of the names in the output.
'''


def filter(list_of_names: [str]) -> [str]:
    return [name for name in list_of_names if len(name) == 4]
