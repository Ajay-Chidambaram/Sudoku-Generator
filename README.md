# Sudoku-Generator

A Program to generate a sudoku puzzle which will have a unique solution

Before you start, you will need Python on your computer.

Check whether you already have an up to date version of Python installed by entering `python` in a command line window

## Run From Command Line 

you can directly run the python code from the command line itself by using the following code

```
python sudoku.py
```

It will generate a Actual Solution and also a Puzzle by removing some elements in it thereby providing a unique solution

You can also specify the difficulty level using the `-d` or `--difficulty` optional flag , which need int as an argument it should range from 1 to 3 as 1 being the easy one

Usage is as follows ,

```
python sudoku.py -d 3
```

## Puzzle GUI

Inorder to get puzzle gui you need pygame in your system, if not install it using `pip` command as follows

```
pip install pygame
```

Then the run the gui.py script 

```
python gui.py
```

you will get output as an png image which will be saved in your current directory as Sudoku-puzzle , just for the purpose of showing the puzzle to the users.

![alt text](https://github.com/Ajay-Chidambaram/Sudoku-Generator/blob/main/Images/sudoku_pygame.PNG)

## Import as Module

This program can able to import in another programs also and it can return the puzzle grid by calling a method `main()`

Usage is as follows :

```python
import sudoku

dimension = 9            # Dimension of the Grid
difficulty = 2            # Difficulty of the Puzzle ranges from ( 1 - 7 ) as 1 being the Lowest
object = sudoku.Sudoku(dimension, difficulty)
puzzle_grid = object.main()
```

## Test Cases

So far i added two test cases in the test_sudoku.py file which consists of one puzzle which is automatically generated puzzle and the test program checks that it has only one solution or not , then the second test case is custom input by the user where the user has to provide a puzzle in 2D list format.

You can run it using pytest , initially check whether `pytest` is in the system, if not present install using `pip` command

```
pip install pytest
```

Then run the test_sudoku.py script as follows :

```
pytest test_sudoku.py
```
