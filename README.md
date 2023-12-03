# advent_of_code_23
https://adventofcode.com/2023

## Day 1
- Part 1: Straightforward looping over strings.
- Part 2: Made a mess of this! Initially I just replaced "one" with "1" and so on, but that relies on the order, so "twone" gives "tw1" when it should notice that there is a "two" first. Then I got stuck because I read the instruction as meaning "twone" should translate to "2ne", but actually it should be "21" as it shares the "o". I thought this was a bit hard for day 1 :D

Internet tip: going through the string using `enumerate` and `startswith` rather than `endswith` makes "twone" trivial.

## Day 2
- Part 1: Breaking up the string into the "hands" was busy work, then it is a case of looping to find the maximum of each colour and checking if it fulfils the condition.
- Part 2: Falls out of part 1 naturally.

## Day 3
- Part 1: Go through each row and if it is a digit check it is valid by looking for surrounding symbols. Also, need to keep track of consecutive digits as that creates the actual number we need.
- Part 2: Modify the code for part 1 to check for asterisks as that could be a potential cog. Collect the possible cogs and see which ones are valid and calculate the result.

## Day 4
- Part 1: .
- Part 2: .

## Day 5
- Part 1: .
- Part 2: .

## Day 6
- Part 1: .
- Part 2: .

## Day 7
- Part 1: .
- Part 2: .

## Day 8
- Part 1: .
- Part 2: .

## Day 9
- Part 1: .
- Part 2: .

## Day 10
- Part 1: .
- Part 2: .
