To run the program simply run the python code either for forwardchecking.py or
backtracking.py; which ever one you want to test.

Running without arguments, will randomly generate a 8x8 puzzle and solve it
with the 'most constrained' heuristic.

to change the heuristic use the
--heuristic parameter. Valid arguments include (without quotes) 'random',
'constrained' and 'constraining'. for example:
--heuristic random

if you would like to randomly generate a puzzle with varied sizes, use the
--width and --height arguments

if you are randomly generating a puzzle, you can see the solution that was
generated with the puzzle by using the -s parameter

if you would like to run with your own input, use a text file.
You can use the argument:
--input along with the typed file name. For example:
--input input.txt

input text files MUST be formatted in this format
with no empty lines after the last line of the puzzle:
# Start of puzzle
8 8
_1_0_1_1
___2____
____101_
2_2_1___
__010___
20_0____
_3____10
____01__


Here is a summary of our algorithms and heuristics:

Backtracking: The domain for backtracking is '_' and 'b'. The function is a
  recursive function. It places bulbs and blanks while moves are still 'legal'.
  if the move is not legal/there is no more room for moves it backtracks and
  continues on. The vertices are the places that we can put bulbs

Forwardchecking: We implemented forwardchecking similar to how it is in the notes.
  After every time the backtracking algorithm adds either a bulb or a blank,
  the forwardchecking algorithm checks to see if any cells cannot be either
  blank or bulb. If there are any cells that cant be either '_' or 'b', then
  the algorithm triggers a backtrack

Random: The random heuristic randomly grabs one of the unassigned cells.

Most Constrained: The Most Constrained heuristic grabs the cell that appears
  to be the most constrained. The constrained priority is calculated from a
  combination of weights from adjacent walls, adjacent beams of light and whether
  the cell is a corner or an edge

Most Constraining: The Most Constraining Heuristic grabs the cell that will impact
  the most cells if that cell were to be assigned. The priority is calculated by
  checking how many cells each cell could light up (that are not currently lit).
