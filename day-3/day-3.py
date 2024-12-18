#!/usr/bin/python3

import re

resulat_puzzle_part1 = 0

# Ouvre le fichier en mode lecture
nom_fichier = 'puzzle-input.txt'
with open(nom_fichier, 'r') as fichier:
    # Lit chaque ligne du fichier
    for ligne in fichier:
        for oper in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)', ligne):
            nums = re.findall(r'\d+', oper)
            resulat_puzzle_part1 += int(nums[0]) * int(nums[1])

print ("Day3 - Part1: ", resulat_puzzle_part1)

multiply = True
resulat_puzzle_part2 = 0

with open(nom_fichier, 'r') as fichier:
    # Lit chaque ligne du fichier
    for ligne in fichier:
        for oper in re.findall(r'mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don\'t\(\)', ligne):
            if oper == "do()":
                multiply = True
            if oper == "don't()":
                multiply = False
            nums = re.findall(r'\d+', oper)
            if multiply and len(nums) > 0:
                resulat_puzzle_part2 += int(nums[0]) * int(nums[1])

print ("Day3 - Part2: ", resulat_puzzle_part2)