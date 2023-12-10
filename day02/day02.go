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
	//file, err := os.Open("sample.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	if err != nil {
		log.Fatal(err)
	}

	//valid_games_sum := 0
	power := 0
	cube_count_map := map[string]int{}

	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		game := strings.Split(line, ":")
		sets := strings.Split(game[1], ";")
		fmt.Println(game[0])

		for _, set := range sets {
			fmt.Println(set)
			set = strings.TrimSpace(set)
			cubes := strings.Split(set, ", ")
			for _, cube_grabs := range cubes {
				cube_count := strings.Split(cube_grabs, " ")
				fmt.Println(cube_count[0], " of ", cube_count[1])
				count, err := strconv.Atoi(cube_count[0])
				if err != nil {
					panic(err)
				}
				if cube_count_map[cube_count[1]] < count {
					cube_count_map[cube_count[1]] = count
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
				fmt.Println("New sum", valid_games_sum)
			}
		*/
		power += cube_count_map["red"] * cube_count_map["blue"] * cube_count_map["green"]
		cube_count_map = make(map[string]int)

	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	//fmt.Println("SUM", valid_games_sum)
	fmt.Println("POWER", power)
}
