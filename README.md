#A* and IDA* algorithms for 8-puzzle and 15-puzzle

requirements: python 3.5
The program can be run from the ommand line as follows:</br>
python puzzleSolver.py \<Algorithm> \<N> </br>
where,</br>
Algorithm:   1 = A* , 2 = IDA* </br>
</br>
N: 3 = 8-puzzle 4 = 15-puzzle format. </br>
INPUT_FILE_PATH = The path to the input file.</br>
OUTPUT_FILE_PATH = The path to the output file.</br>
</br>
It would return an error if any of the command line arguments is missing or N is wrong for a given input.txt
Puzzlesolver is documented in the code itself at a method level.
Output files for both sample inputs 3.txt and 4.txt have been saved into 3_output.txt and 4_output.txt respectively.
</br>
PuzzleGenerator is also included for sake of easy verification.
