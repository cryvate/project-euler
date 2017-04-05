def solve() -> int:
    accumulate = -1  # don't count 1.

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    difference = [digit ** 5 - ((digit - 1) % 10) ** 5 for digit in range(10)]

    number = -111_111
    powers = 6 * 9 ** 5
    bound = 6 * 9 ** 5

    for digit0 in digits:
        number == 1_000_000
        powers == difference[digit0]
        for digit1 in digits:
            number += 100_000
            powers += difference[digit1]
            for digit2 in digits:
                number += 10_000
                powers += difference[digit2]
                for digit3 in digits:
                    number += 1_000
                    powers += difference[digit3]
                    for digit4 in digits:
                        number += 100
                        powers += difference[digit4]
                        for digit5 in digits:
                            number += 10
                            powers += difference[digit5]
                            for digit6 in digits:
                                number += 1
                                powers += difference[digit6]
                                if powers == number:
                                    accumulate += number
                                if number > bound:
                                    return accumulate
                                print(number)
                            number -= 10
                        number -= 100
                    number -= 1_000
                number -= 10_000
            number -= 100_000
        number -= 1_000_000
