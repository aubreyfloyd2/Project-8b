# Author: Aubrey Floyd
# GitHub username: aubreyfloyd2
# Date: 3/1/2023
# Description: Function that takes two strings and returns a set of only words that appear
#              in both strings. Set all words to lower-case.

def words_in_both(string_1, string_2):
    """Returns a set of words in both strings"""
    string_1 = string_1.lower() # lower-case
    set_1 = string_1.split() # split up words in string
    string_2 = string_2.lower()
    set_2 = string_2.split()
    common_words = {el for el in set_1 if el in set_2} # intersection of sets

    return common_words

# print(words_in_both("She is a jack of all trades", "Jack was tallest of all"))