#!/usr/bin/env python3
"""
Author : Adam Bialozyt <adambialko@gmail.com>
Date   : 26.06.2023
Purpose: Simulate the Crows Nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Crows nest simulator',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='Observed object')

    parser.add_argument('-s',
                        '--starboard',
                        help='is it starboard side',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word
    char = word[0]
    article = 'an' if char.lower() in 'aeiou' else 'a'
    article = article.title() if char.isupper() else article

    side = 'starboard' if args.starboard else 'larboard'

    phrase = f'Ahoy, Captain, {article} {word} off the {side} bow!'

    print(phrase)


# --------------------------------------------------
if __name__ == '__main__':
    main()
