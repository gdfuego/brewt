#!/usr/bin/env python

"""Script for generating password possibilities"""

def setup():
    """parse arguments"""
    import argparse
    parser = argparse.ArgumentParser(description='usage: %prog [options]')
    parser.add_argument('--passfile', '-p', default=False, required=True,
                        help="File containing password list.  One per line.")
    parser.add_argument('--minwords', default=1, type=int,
                        help="Minimum number of words to use in combinations.")
    parser.add_argument('--maxwords', type=int,
                        help="Maximum number of words to use in combinations.")
    args = parser.parse_args()
    return args

def generate_list(wordlist, min_words, max_words):
    """Cycle through each password, then all permutations of combining two
    passwords, then 3, etc up to the length of the array."""
    from itertools import permutations
    mylist = []
    for i in xrange(min_words, max_words):
        for current_option in permutations(wordlist, i):
            mylist.append(''.join(current_option))
    return mylist

def main():
    """Non-module logic for running as a commandline tool"""
    options = setup()

    wordlist = []
    # Build an array of all known passwords
    file_handle = open(options.passfile)
    for line in file_handle.readlines():
        wordlist.append(line.strip('\n'))

    if options.maxwords:
        maxwords = options.maxwords
    else:
        # Add 1 since the length is 0 indexed
        maxwords = len(wordlist)

    for word in generate_list(wordlist, options.minwords, maxwords):
        print word

if __name__ == '__main__':
    main()
