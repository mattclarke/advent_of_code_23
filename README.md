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
- Part 1: Simple to implement algorithm.
- Part 2: Slight adjustment to algorithm to use multiple paths. Would take a long time for all to be at a finish at the same time, so time each individually and then calculate the LCM for the individual results. I thought it would be the LCM but somehow I got the wrong result, so disappeared down a rabbit hole for a few hours. Then I tried the LCM again and got the correct answer :(

## Day 9
- Part 1: Implement algorithm by only keeping the last values and once the difference is calculated go throught the last values increasing them by the differencr.
- Part 2: Adjust the algorithm to track the first values and essentially do the same thing but subtracting.

## Day 10
- Part 1: Pretty straightforward: from `S` start counting in both directions and continue until there is no more pipe to count .
- Part 2: There is probably a much simpler way to solve this than my method.
First, use the data from part 1 to remove any parts of pipe that is not connected to the main loop.
Then go around the loop in one direction and assign any empty space on the left (relative to the direction of travel) as "A" and empty spaces on the right as "B".
Flood fill the remaining empty spaces with whichever letter they are adjacent to.
Finally, count up the number of As and Bs - the lowest value will be the number of squares enclosed as it is smaller than the area outside.

Better solution is to use the 'line counting' algorithm, see the bottom of the code file for an implementation.

## Day 11
- Part 1: Sufficient to just crudely expand the input on the empty rows and columns.
- Part 2: The expansion of empty rows and columns is now too big to do crudely
Instead we track which rows and columns are empty, and we calculate how many we cross when measuring the distance on the unexpanded layout and add 1,000,000 for each one.

## Day 12
- Part 1: Recursion.
- Part 2: Big input, but can using caching to make it quick. It took me a while to get the caching to work correctly.

## Day 13
- Part 1: Simple enough to find the reflection. For the columns we rotate the layout by 90 degrees.
- Part 2: Stuck for ages (a good night's sleep helps!). The key is to ignore the original reflection when searching for a reflections otherwise if the original appears before the new one we don't get to the new one. Simply really...

## Day 14
- Part 1: Create the algorithm for tilting north and run it once.
- Part 2: Create the algorithm for the other directions. The puzzle requires to run it for a long time, but it starts to repeat, so once it does we can use the repeat period to shortcut the loop.
Used a dictionary to represent the layout - it might not be the most efficient data structure to use, but it finishes in a few seconds, so meh.

## Day 15
- Part 1: Implement the hashing algorithm.
- Part 2: Using a dictionary of dictionaries makes this trivial as Python's dictionary maintains the insertation order.

## Day 16
- Part 1: The algorithm is pretty simple to implement; I use a queue for adding an extra direction when hitting a splitter. The only catch was that some of the light can loop forever, so I used a set to determine if the light was reaching an already visited position whilest travelling in the same direction, if so then stop.
- Part 2: Move the code from part 1 into a function that takes a start position and a direction and then try starting the light from all of the edges one by one and track the maximum.

## Day 17
- Part 1: Initially just did BFS but biasing it towards unvisited squares, it is slow though (pypy ~7 minutes for both parts). Changing it to use a heapq is much quicker (pypy ~7 seconds for both parts).
- Part 2: Slight modification to algorithm.

## Day 18
- Part 1: Simple enough to use a set to sketch the outline and then fill in the internal space.
- Part 2: Much bigger numbers so had to rewrite part 1. Keep track of the vertical lines and the corners, and then using the "line counting" algorithm from day 10 to work out which squares are in and out.
The complicated part is the rows where corners appear as we need to work out whether the corner represents going through a wall or not.

My solution takes ~45 seconds with Pypy, but I can speed it up with maths!

## Day 19
- Part 1: .
- Part 2: .

## Day 20
- Part 1: .
- Part 2: .

## Day 21
- Part 1: .
- Part 2: .

## Day 22
- Part 1: .
- Part 2: .

## Day 23
- Part 1: .
- Part 2: .

## Day 24
- Part 1: .
- Part 2: .

## Day 25
- Part 1: .
- Part 2: .
