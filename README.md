# wordfind

A project to generate crossword puzzles using Python.
The project currently consists of one file, wordfind.py, containing the Wordfind class, and another file, run.py, meant to run the functions in the class to generate a puzzle.

The class contains functions that can
- Generate a blank grid
- Insert words into the grid, with position specified as location of first letter and direction.
- Check if a word cannot be placed due to out of bounds or intersection issues.
- Populate the remaining grid with random letters.

The biggest issue at present would be ensuring that filling up the grid does not cause more words to appear than intended.
Any changes and additions are welcome.
