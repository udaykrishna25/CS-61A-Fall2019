"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    lst = []
    if k > len(paragraphs) == True:
        return ""

    for i in paragraphs:
        if select(i) == True:
            lst += [i]
    if k >= len(lst):
        return ""
    else:
        return lst[k]
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    lst = []
    def select(paragraphs):
        paragraph = split(lower(remove_punctuation(paragraphs)))
        if len(paragraph) == 0:
            return ""
        else:
            for i in paragraph:
                if i in topic:
                    return True
        return False
    return select


    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    count = 0
    if typed == "":
        return 0.0

    for i in range(min(len(typed_words),len(reference_words))):
        if typed_words[i] == reference_words[i]:
            count += 1

    return count/len(typed_words) * 100
    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    return float(((len(typed)/5)/elapsed)*60)
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    lst = []
    if user_word in valid_words:
        return user_word
    else:
        for i in valid_words:
            lst.append(diff_function(user_word, i, limit))
        if min(lst) > limit:
            return user_word
        else:
            return valid_words[lst.index(min(lst))]
    # END PROBLEM 5


def swap_diff(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    def helper(start,goal,limit,old_limit):
        if limit < 0:
            return old_limit + 1
        elif len(start) == 0:
            return len(goal)
        elif len(goal) == 0:
            return len(start)
        else:
            if start[0] == goal[0]:
                return helper(start[1:],goal[1:],limit, limit)
            else:
                return 1 + helper(start[1:],goal[1:],limit - 1, limit)

    return helper(start,goal,limit,limit)
    # END PROBLEM 6

def edit_diff(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL."""

    if not start or not goal:
        return len(goal) + len(start)

    elif start[0] == goal[0]:
        return edit_diff(start[1:],goal[1:],limit)

    if limit < 0:
        return limit + 1

    else:
        add_diff = 1 + edit_diff(start, goal[1:], limit - 1)
        remove_diff = 1 + edit_diff(start[1:], goal, limit - 1)
        substitute_diff = 1 + edit_diff(start[1:], goal[1:], limit - 1)

    return min(add_diff,remove_diff,substitute_diff)

def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'




###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    n = 0
    count = 0
    while n < min(len(prompt),len(typed)):
        if typed[n] == prompt[n]:
            count += 1
        else:
            n += min(len(prompt),len(typed)) + 1
        n +=1
    ratio = count/len(prompt)
    send({'id': id, 'progress': ratio})
    return ratio

    # END PROBLEM 8


def fastest_words_report(word_times):
    """Return a text description of the fastest words typed by each player."""
    fastest = fastest_words(word_times)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def fastest_words(word_times, margin=1e-5):
    """A list of which words each player typed fastest."""
    n_players = len(word_times)
    n_words = len(word_times[0]) - 1
    assert all(len(times) == n_words + 1 for times in word_times)
    assert margin > 0
    # BEGIN PROBLEM 9
    def time_spent_typing_word(k, player):
        return elapsed_time(word_times[player][k+1]) - elapsed_time(word_times[player][k])

    def fastest_time_for_word(k):
        time = [time_spent_typing_word(k,player) for player in range(n_players)]
        return min(time)

    players_lst = []
    for player in range(n_players):
        player_lst = []
        for nth_word in range(n_words):
            min_time = fastest_time_for_word(nth_word)
            if abs(min_time - time_spent_typing_word(nth_word,player)) <= margin:
                player_lst = player_lst + [word(word_times[player][nth_word + 1])]
        players_lst = players_lst + [player_lst]
    return players_lst
    # END PROBLEM 9


def word_time(word, elapsed_time):
    """A data abstrction for the elapsed time that a player finished a word."""
    return [word, elapsed_time]


def word(word_time):
    """An accessor function for the word of a word_time."""
    return word_time[0]


def elapsed_time(word_time):
    """An accessor function for the elapsed time of a word_time."""
    return word_time[1]


enable_multiplayer = False  # Change to True when you


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)
