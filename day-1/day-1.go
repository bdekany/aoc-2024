package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"sort"
	"strconv"
	"slices"
)


func main() {
	// Ouvrir le fichier
	file, err := os.Open("puzzle-input.txt")
	if err != nil {
		fmt.Println("Erreur lors de l'ouverture du fichier:", err)
		return
	}
	defer file.Close()


	var result_part1 int
	var result_part2 int
	var column_one []int
	var column_two []int

	// Transferer les deux listes dans deux slices
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		args := strings.Split(line, "   ")
		one, _ := strconv.Atoi(args[0])
		two, _ := strconv.Atoi(args[1])
		column_one = append(column_one, one)
		column_two = append(column_two, two)
	}

	// Trier les slices
	sort.Ints(column_one)
	sort.Ints(column_two)

	// calcul des ecrats (part1)
	result_part1 = 0
	for n := range column_one {
		if column_one[n] < column_two[n] {
			result_part1 += column_two[n] - column_one[n]
		} else {
			result_part1 += column_one[n] - column_two[n]
		}
	}


	// Recheche indexes
	result_part2 = 0
	for _, val := range column_one {
		multiply := 0

		for {
			n := slices.Index(column_two, val)
			if n == -1 {break}
			multiply++
			slices.Delete(column_two, n, n+1 )
		}

		result_part2 += val * multiply

	}


	fmt.Println("Day 1 - Part 1: ", result_part1)
	fmt.Println("Day 1 - Part 2: ", result_part2)
}