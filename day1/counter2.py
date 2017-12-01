import sys


def sum_recurring_digits(sequence: str):
    """
    Reviews a sequence of digits and finds the sum of all digits
    that match digit halfway around the circular list.
    """
    total = 0
    i = 0
    length = len(sequence)

    while i < length:
        digit = int(sequence[i])
        next_digit_index = int(i + (length / 2))

        if next_digit_index + 1 > length:
            next_digit_index -= length

        next_digit = int(sequence[next_digit_index])

        if digit == next_digit:
            total += digit

        i += 1

    return total


def test():
    assert sum_recurring_digits('1212') == 6
    assert sum_recurring_digits('1221') == 0
    assert sum_recurring_digits('123425') == 4
    assert sum_recurring_digits('123123') == 12
    assert sum_recurring_digits('12131415') == 4


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
