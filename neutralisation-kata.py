'''
Given two strings comprised of + and -, return a new string which shows how the two strings interact in the following way:

When positives and positives interact, they remain positive.
When negatives and negatives interact, they remain negative.
But when negatives and positives interact, they become neutral, and are shown as the number 0.

Worked Example
("+-+", "+--") ➞ "+-0"

# Compare the first characters of each string, then the next in turn.
# "+" against a "+" returns another "+".
# "-" against a "-" returns another "-".
# "+" against a "-" returns "0".
# Return the string of characters.

Examples
("--++--", "++--++") ➞ "000000"

("-+-+-+", "-+-+-+") ➞ "-+-+-+"

("-++-", "-+-+") ➞ "-+00"
'''


def neutralise(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        return "Strings must be of equal length"
    if len(str1) == 0:
        return ""
    return ''.join('+' if i == j == '+' else '-' if i == j == '-' else '0' for i, j in zip(str1, str2))
