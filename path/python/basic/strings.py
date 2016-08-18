#!/usr/bin/env python3

print('spam eggs')
print('doesn\'t')  # use \' to escape the single quote
print("doesn't")
print('"Yes", he said.')
print('"Isn\'t", she said.')
print()

print('First line.\nSecond line.')  # \n means newline
print()

print('C:\some\name')  # here \n means newline
print(r'C:\some\name')  # note the r before the quote
print()

# triple quotes include newlines in string, prevent by adding \ before newline
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to

""")

print('Py' + 'thon')  # concatenate with +
print(3 * 'un' + 'ium')  # repeat with *
print('Py' 'thon')  # adjacent string literals concatenate
text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print()

word = 'Python'
print("word = 'Python'")
print("word[0] = ", word[0])
print("word[5] = ", word[5])
print("word[-1] = ", word[-1])  # last character
print("word[-2] = ", word[-2])  # second to last character
print("word[-6] = ", word[-6])
print()

#  +---+---+---+---+---+---+
#  | P | y | t | h | o | n |
#  +---+---+---+---+---+---+
#  0   1   2   3   4   5   6
# -6  -5  -4  -3  -2  -1
print("word = 'Python'")
print('word[0:2] = ', word[0:2])
print('word[:2] = ', word[:2])   # default to zero
print('word[4:] = ', word[4:])   # default to length of string
print('word[2:5] = ', word[2:5])
print('word[:2] + word[2:] = ', word[:2] + word[2:])
print('word[:4] + word[4:] = ', word[:4] + word[4:])
print()

s = 'supercalifragilisticexpialidocious'
print('len({}) = '.format(s), len(s))
