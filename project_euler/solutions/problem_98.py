from collections import Counter
from itertools import combinations, permutations

from typing import List

from ..framework.load_file import load_file
from ..library.sequences import square_sequence
from ..library.sqrt import is_square_fast as is_square
from ..library.base import list_to_number

square_endings = [(i ** 2) % 10 for i in range(10)]


def find_square_representations(word1: str, word2: str) -> int:
    letters = sorted(set(word1))

    word_in_int1 = []
    word_in_int2 = []

    for letter in word1:
        word_in_int1.append(letters.index(letter))

    for letter in word2:
        word_in_int2.append(letters.index(letter))

    squares = [0]

    for combination in combinations(range(10), len(letters)):
        for permutation in permutations(combination):
            end = permutation[word_in_int1[-1]]
            if end not in (0, 1, 4, 5, 6, 9):
                continue

            end = permutation[word_in_int2[-1]]
            if end not in (0, 1, 4, 5, 6, 9):
                continue

            if permutation[word_in_int1[0]] == 0:
                continue

            if permutation[word_in_int2[0]] == 0:
                continue

            word_in_new1 = []
            for letter in word_in_int1:
                word_in_new1.append(permutation[letter])

            new_int1 = list_to_number(word_in_new1)

            if not is_square(new_int1):
                continue

            word_in_new2 = []
            for letter in word_in_int2:
                word_in_new2.append(permutation[letter])

            new_int2 = list_to_number(word_in_new2)

            if is_square(new_int2):
                squares.append(max(new_int1, new_int2))

    return max(squares)



def solve() -> int:
    words = load_file(98, 'words.txt').strip('"').split('","')

    anagrams = {}
    counter = Counter()

    for word in words:
        canonical = tuple(sorted(word))

        if canonical not in anagrams:
            anagrams[canonical] = []

        anagrams[canonical].append(word)
        counter[canonical] += 1

    anagrams = {key: value for key, value in anagrams.items() if counter[key] >= 2}

    max_length = max(len(key) for key in anagrams)

    bound = 10 ** max_length

    squares = []

    for square in square_sequence():
        if square >= bound:
            break

        squares.append(square)

    largest = 0
    largest_length = None

    for canonical, words in sorted(anagrams.items(),
                                   key=lambda item: -len(item[0])):
        if largest_length is not None and largest_length > len(canonical):
            break

        for word1 in words:
            for word2 in words:
                if word2 >= word1:
                    break

                found = find_square_representations(word1, word2)

                if found > 0 and found > largest:
                    largest = found

                    largest_length = len(canonical)

    return largest
