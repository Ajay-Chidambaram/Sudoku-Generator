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

## Puzzle GUI

Inorder to get puzzle gui you need pygame in your system, if not install it using `pip` command as follows

```
pip install pygame
```

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
