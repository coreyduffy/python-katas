'''
Task
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]

Notes
"flick" will always be given in lowercase.
A list may contain multiple flicks.
Switch the boolean value on the same element as the flick itself.
'''

def flick_switch(list_of_words: [str]) -> [bool]:
    bool_value_to_return = True
    result = []
    for word in list_of_words:
        if word == "flick":
            bool_value_to_return = not bool_value_to_return
        result.append(bool_value_to_return)
    return result
