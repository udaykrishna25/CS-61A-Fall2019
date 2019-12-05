"Utility functions for file and string manipulation"

import string


def lines_from_file(path):
    """Return a list of strings, one for each line in a file."""
    with open(path, 'r') as f:
        return [line.strip() for line in f.readlines()]


punctuation_remover = str.maketrans('', '', string.punctuation)


def remove_punctuation(s):
    """Return a string with the same contents as s, but with punctuation removed.

    >>> remove_punctuation("It's a lovely day, don't you think?")
    'Its a lovely day dont you think'
    """
    return s.strip().translate(punctuation_remover)


def lower(s):
    """Return a lowercased version of s."""
    return s.lower()


def split(s):
    """Return a list of words contained in s, which are sequences of characters
    separated by whitespace (spaces, tabs, etc.).

    >>> split("It's a lovely day, don't you think?")
    ["It's", 'a', 'lovely', 'day,', "don't", 'you', 'think?']
    """
    return s.split()

if limit < 0: # Fill in the condition
    # BEGIN
    return limit + 1
    # END

elif : # Feel free to remove or add additional cases
    # BEGIN
    "*** YOUR CODE HERE ***"
    # END

else:
    add_diff = ...  # Fill in these lines
    remove_diff = ...
    substitute_diff = ...
    # BEGIN
    "*** YOUR CODE HERE ***"
    # END


count = 0
for i in range(min(len(typed),len(prompt))):
    if typed[i] == prompt[i]:
        count += 1
    else:

def helper(start, goal, len_start, len_goal, limit, old_limit):

    if limit < 0:
        return old_limit + 1

    elif len_start == 0:
        return len_goal

    elif len_goal == 0:
        return len_start

    elif start[len_start - 1] == goal[len_goal - 1]:
        return helper(start,goal, len_start - 1, len_goal - 1, limit, limit)

    else:
        1 + min(helper(start, goal, len_start, len_goal - 1, limit - 1, limit), helper(start, goal, len_start - 1, len_goal, limit - 1, limit), helper(start, goal, len_start - 1, len_goal - 1, limit - 1, limit))

return helper(start, goal, len(start), len(goal), limit, limit)
