package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
	"strconv"
	"slices"
)

func isSafe(s []string) bool {
	// convertion integer
	var report []int
	for _, a := range s {
		i, _ := strconv.Atoi(a)
		report = append(report, i)
	}

	/*
	The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
	*/
	report_reverse := slices.Clone(report)
	slices.Reverse(report_reverse)

	if slices.IsSorted(report) == false && slices.IsSorted(report_reverse) == false {
		return false
	}

	for n, _ := range report {
		if n == len(report)-1	 { break }

		pente := report[n] - report[n+1]
		if pente == 0 || pente > 3 || pente < -3 {
			return false
		}
	}

	return true


}

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

	var reports [][]string

	// Transferer les rapports
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()

		reports = append(reports, strings.Split(line, " "))
	}

	result_part1 = 0
	result_part2 = 0

	for _, s := range reports {
		if isSafe(s) {
			result_part1++
			result_part2++
		} else {
			for n, _ := range s {
				
				if n == len(s) { break }
				t := slices.Clone(s)
				t = slices.Delete(t, n, n+1)
				
				if isSafe(t) {
					result_part2++
					break
				}
			}
		}
	}

	fmt.Println("Day 2 - Part 1: ", result_part1)
	fmt.Println("Day 2 - Part 2: ", result_part2)
}