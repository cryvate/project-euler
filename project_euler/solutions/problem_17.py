NAMES = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
         'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
         'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
NAMES_LENGTH = [len(name) for name in NAMES]

NAMES_TENS = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
              'seventy', 'eighty', 'ninety']
NAMES_TENS_LENGTH = [len(name) for name in NAMES_TENS]


def letters_in_number(n: int) -> int:
    if n <= 0 and n > 1000:
        raise ValueError(f'Unsupported input {n}, should be 1 <= n <= 1000.')
    elif n < 20:
        return NAMES_LENGTH[n]
    elif n < 100:
        return NAMES_LENGTH[n % 10] + NAMES_TENS_LENGTH[n // 10]
    elif n < 1000:
        if n % 100 == 0:
            return NAMES_LENGTH[n // 100] + len('hundred')
        else:
            return NAMES_LENGTH[n // 100] + len('hundred') + len('and') + \
                   letters_in_number(n % 100)
    elif n == 1000:
        return len('one') + len('thousand')


def solve(bound: int=1000) -> str:
    return sum(letters_in_number(n) for n in range(1, bound + 1))
