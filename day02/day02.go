/* First time using Go */
package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const MAX_RED int = 12
const MAX_GREEN int = 13
const MAX_BLUE int = 14

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	//valid_games_sum := 0
	power := 0
	cube_counts := map[string]int{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		// Game 31: 8 red, 16 blue; 2 red, 1 green, 1 blue; 5 red, 8 blue, 1 green
		game := strings.Split(line, ":")
		sets := strings.Split(game[1], ";")

		for _, set := range sets {
			cube_grabs := strings.Split(strings.TrimSpace(set), ", ")
			for _, cubes := range cube_grabs {
				cubes_color_and_count := strings.Split(cubes, " ")

				count, err := strconv.Atoi(cubes_color_and_count[0])
				if err != nil {
					panic(err)
				}

				color := cubes_color_and_count[1]

				if cube_counts[color] < count {
					cube_counts[color] = count
				}
			}
		}
		// Part 1
		/*
			if cube_count_map["green"] > MAX_GREEN || cube_count_map["red"] > MAX_RED || cube_count_map["blue"] > MAX_BLUE {
				fmt.Println("Too many", cube_count_map)
			} else {
				game_id := strings.Split(game[0], " ")
				game_id_int, err := strconv.Atoi(game_id[1])

				if err != nil {
					panic(err)
				}
				valid_games_sum += game_id_int
			}
		*/
		power += cube_counts["red"] * cube_counts["blue"] * cube_counts["green"]
		cube_counts = make(map[string]int)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	//fmt.Println("SUM", valid_games_sum)
	fmt.Println("POWER", power)
}
