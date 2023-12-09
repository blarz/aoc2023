import re
import sys

example = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

example_part2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

overlap = "twone"

spelled_out = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}


digits_and_spelled_out_re = re.compile(
    r'(?=(\d|' + '|'.join(spelled_out.keys()) + '))'
)


def to_digit(d):
    return int(d) if d.isnumeric() else spelled_out[d]


def calibration_sum(lines):
    sum = 0
    for line in lines:
        digits = digits_and_spelled_out_re.findall(line)

        first = to_digit(digits[0])
        second = to_digit(digits[-1])
        sum += first*10 + second

    return sum


def main(argv):
    if len(argv) != 1:
        exit(-1)

    with open(argv[0]) as input:
        lines = input.readlines()
        print(f"Sum: {int(calibration_sum(lines))}")


if __name__ == "__main__":
    main(sys.argv[1:])
