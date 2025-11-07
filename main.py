#refactoring means to
# -improve the structure of existing code
# - without changing its external behavior
# This helps enchance code readability
# maintainability, and efficiency.

from problem_set_1 import problem1
from advanced_slicing import advanced_slice
from problem_set_2 import problem2
from Manipulating_Words import Manipulating_Words
from problem_set_3 import problem3
from replacing_words import replacing_words
from problem_set_4 import problem4
from word_search import word_search
from Length_and_Count import LengthandCount


problem1( )
advanced_slice( )
problem2( )
Manipulating_Words( )
problem3( )
replacing_words( )
problem4( )
word_search( )
LengthandCount( )


# c. Reverse the entire string using slicing.
reserved_string = alphabet[::2] # If you p[ut a negative into a [::-1] then it reverses a string
print(reserved_string)


# c. Reverse the positions of the words, but keep the characters in each word in the same order.
Reserved_word_positions= info.split()[::-1]

