import sys


def sum_recurring_digits(sequence: str):
    """
    Reviews a sequence of digits and finds the sum of all digits that match the
    next digit in the list. The list is circular, so the digit after the last
    digit is the first digit in the list.
    """
    total = 0
    i = 0
    count = len(sequence)

    while i < count:
        digit = int(sequence[i])
        if i + 1 < count:
            next_digit = sequence[i + 1]
        else:
            # the list is circular,
            # check the first digit
            next_digit = sequence[0]
        next_digit = int(next_digit)

        if digit == next_digit:
            total += digit

        i += 1

    return total


def test():
    assert sum_recurring_digits('1122') == 3
    assert sum_recurring_digits('1111') == 4
    assert sum_recurring_digits('1234') == 0
    assert sum_recurring_digits('91212129') == 9


if __name__ == '__main__':
    if len(sys.argv) == 2:
        sequence = sys.argv[1]
    else:
        sequence = sys.stdin.read().strip()

    if not sequence:
        print("Usage: python counter.py < <input>")
        exit(1)

    if sequence == 'test':
        print('Running tests')
        test()

    else:
        result = sum_recurring_digits(sequence)
        print('Result: {}'.format(result))
