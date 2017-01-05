

The program should run from the command line as follows:    <\br>
python puzzleSolver.py <#Algorithm> <N> <INPUT_FILE_PATH> <OUTPUT_FILE_PATH> <\br>
where,
#Algorithm: 1 = A* and 2 = Memory bounded variant(IDA*)
N: 3 = 8-puzzle 4 = 15-puzzle format.
INPUT_FILE_PATH = The path to the input file.
OUTPUT_FILE_PATH = The path to the output file.


It would return an error if any of the command line arguments is missing or N is wrong for a given input.txt
Puzzlesolver is documented in the code itself at a method level.
Output files for both sample inputs 3.txt and 4.txt have been saved into 3_output.txt and 4_output.txt respectively.

PuzzleGenerator is also included for sake of easy verification.

