import sys


def part_sums(lines):
    sum = 0
    number_of_lines = len(lines)
    for line_index, line in enumerate(lines):
        part_number = ""
        adjacent = False
        for char_index, char in enumerate(line):
            line_length = len(line.rstrip())
            if not char.isdigit():
                if len(part_number) > 0 and adjacent:
                    print(f"Adding \"{part_number}\"")
                    sum += int(part_number)
                part_number = ""
                adjacent = False
            else:
                # It's a digit
                part_number += char

                surroundings = [
                    # Below
                    (line_index+1, char_index),
                    # Below right
                    (line_index+1, char_index+1),
                    # Below left
                    (line_index+1, char_index-1),
                    # Above
                    (line_index-1, char_index),
                    # Above right
                    (line_index-1, char_index+1),
                    # Above left
                    (line_index-1, char_index-1),
                    # Left
                    (line_index, char_index-1),
                    # Right
                    (line_index, char_index+1),
                ]

                for coordinates in surroundings:
                    if coordinates[0] < 0 or coordinates[1] < 0:
                        continue
                    if coordinates[0] >= number_of_lines \
                            or coordinates[1] >= line_length:
                        continue
                    adjacer = lines[coordinates[0]][coordinates[1]]
                    if not adjacer.isdigit() and adjacer != ".":
                        adjacent = True
                        print(f"ZOMG {char} adjaces to {adjacer}")

    return sum


def main(argv):
    if len(argv) != 1:
        exit(-1)

    with open(argv[0]) as input:
        lines = input.readlines()
        print(f"Sum: {int(part_sums(lines))}")


if __name__ == "__main__":
    main(sys.argv[1:])
