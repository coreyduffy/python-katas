'''
Task:
Your job here is to implement a function factors, which takes a number n, and outputs an array of arrays comprised of two parts, sq and cb. The part sq will contain all the numbers that, when squared, yield a number which is a factor of n, while the cb part will contain all the numbers that, when cubed, yield a number which is a factor of n. Discard all 1s from both arrays.

Both sq and cb should be sorted in ascending order.

What it looks like:
factors(int) #=> [
  sq (all the numbers that can be squared to give a factor of n) : list,
  cb (all the numbers that can be cubed   to give a factor of n) : list
]
Some examples:
factors(1) #=> [[], []]
  # ones are discarded from outputs

factors(4) #=> [[2], []]
  # 2 squared is 4;   4 is a factor of 4

factors(16) #=> [[2, 4], [2]]
  # 2 squared is  4;  4 is a factor of 16
  # 4 squared is 16; 16 is a factor of 16
  # 2 cubed is    8;  8 is a factor of 16

factors(81) #=> [[3, 9], [3]]
  # 3 squared is  9;  9 is a factor of 81
  # 9 squared is 81; 81 is a factor of 81
  # 3 cubed is   27; 27 is a factor of 81
'''


def factors(value: int) -> [[int]]:
    if value == 1:
        return [[], []]
    num = 2
    square_factors = []
    cube_factors = []
    while (True):
        square = num * num
        cube = num * num * num
        if num * num > value:
            break
        if value % square == 0:
            square_factors.append(num)
        if value % cube == 0:
            cube_factors.append(num)
        num += 1
    return [square_factors, cube_factors]
