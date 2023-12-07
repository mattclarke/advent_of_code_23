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
- Part 1: Extract the ticket information and use sets to calculate the number of wins.
- Part 2: Cache the number of wins per hand during part 1. Use a list to keep track of the number of cards for each card type, then go through each card assigning wins until we reach the final card.

Update: Part 2 is simpler than I thought: the number of cards never increases (reading fail), so much less code required.

## Day 5
- Part 1: Simple enough to use brute-force to solve.
- Part 2: Takes a while to use brute-force (hours?) with a list of every seed - I accidently left it running during a meeting and came back to find the answer waiting for me! To speed it up, we just track the starts and ends rather than each individual seed; however, they increase in numbers significantly as the rules are applied which makes it very slow.
E.g.
```
seed range = [10, 20] and the rule is "12 to 16 increase by 10" then we end up with three seed ranges
=> [10, 12], [22, 26], [17, 20]
```
To speed the program up, we "join" the seed ranges that either overlap or are contiguous, e.g.
```
ranges = [10, 20], [19, 30] => [10, 30]
ranges = [10, 20], [21, 30] => [10, 30]
```
Takes less than a second.

Turns out I had a bug which is why it created so many items. Once that was fixed then the optimisations were no longer required :D

## Day 6
- Part 1: Brute-force.
- Part 2: Two binary searches: one to find the lower limit and one to find the higher limit. The t isn't actually that big, so it only takes about 5 seconds to brute-force it.

## Day 7
- Part 1: Counter class FTW. The comparision function is bit of a mess but it works
- Part 2: Same as part 1, but remove the "J"s and add their count to the most common card.

## Day 8
- Part 1: .
- Part 2: .

## Day 9
- Part 1: .
- Part 2: .

## Day 10
- Part 1: .
- Part 2: .
