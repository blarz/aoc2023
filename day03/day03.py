import sys
import re


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


def gear_ratio(lines):
    number_of_lines = len(lines)
    ratio = 0

    asterisk_positions = []
    for line_index, line in enumerate(lines):
        asterisk_positions += [(line_index, asterisk.start())
                               for asterisk in re.finditer(r'\*', line)]
    if not asterisk_positions:
        return 0

    for aster in asterisk_positions:
        print(f"Checking surroundings for * at {aster}")

        surrounding_parts = []
        for line_index in (aster[0], aster[0]+1, aster[0]-1):
            if line_index < 0 or line_index > number_of_lines:
                continue

            for surrounding_match in re.finditer(r'\d*', lines[line_index]):
                if not surrounding_match.group():
                    # Ignore empty matches from finditer...
                    continue
                if aster[1] <= surrounding_match.end() \
                        and aster[1] >= surrounding_match.start()-1:
                    surrounding_parts.append(int(surrounding_match[0]))

        if len(surrounding_parts) == 2:
            print(f"Found exactly 2 parts around {aster}: {surrounding_parts}")
            ratio += surrounding_parts[0] * surrounding_parts[1]

    return ratio


def main(argv):
    if len(argv) != 1:
        exit(-1)

    with open(argv[0]) as input:
        lines = input.readlines()
        # Part 1:
        # print(f"Sum: {int(part_sums(lines))}")
        print(f"Gear Ratio: {int(gear_ratio(lines))}")


if __name__ == "__main__":
    main(sys.argv[1:])
