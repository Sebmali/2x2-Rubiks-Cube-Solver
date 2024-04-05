"""
Test.py
Purpose: This file contains the test cases for the entirety of the Rubiks Cube project.
Should be testing all the moves, the cube class, and the corner class.
Authors: Sebastian Maliczewski, Shayne Prakash
To Run: input "Pytest -s Test.py" in the terminal, and input the file "test.txt" when prompted
"""
from Rubiks import Cube
from Corner import Corner
from Constants import *
from TestConstants import *
from unittest.mock import patch
import pytest
import Main


cube = Cube(True)
unsolved_cube = Cube()

def check_cube(move_cube, cube_to_check):
    for i in range(8):
        for j in range(3):
            if move_cube[i][j] != cube_to_check.get_color(i, j):
                return False
    return True

#---------------------------------------------------------------------
# Test cases for each move

def test_right_vertical_up():
    cube.apply_move(RVU)
    assert check_cube(RVU_CUBE, cube) == True
    cube.undo_move(RVU)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_right_vertical_down():
    cube.apply_move(RVD)
    assert check_cube(RVD_CUBE, cube) == True
    cube.undo_move(RVD)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_left_vertical_up():
    cube.apply_move(LVU)
    assert check_cube(LVU_CUBE, cube) == True
    cube.undo_move(LVU)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_left_vertical_down():
    cube.apply_move(LVD)
    assert check_cube(LVD_CUBE, cube) == True
    cube.undo_move(LVD)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_top_horizontal_right():
    cube.apply_move(THR)
    assert check_cube(THR_CUBE, cube) == True
    cube.undo_move(THR)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_top_horizontal_left():
    cube.apply_move(THL)
    assert check_cube(THL_CUBE, cube) == True
    cube.undo_move(THL)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_bottom_horizontal_right():
    cube.apply_move(BHR)
    assert check_cube(BHR_CUBE, cube) == True
    cube.undo_move(BHR)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_bottom_horizontal_left():
    cube.apply_move(BHL)
    assert check_cube(BHL_CUBE, cube) == True
    cube.undo_move(BHL)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_front_clockwise():
    cube.apply_move(FC)
    assert check_cube(FC_CUBE, cube) == True
    cube.undo_move(FC)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_front_counter_clockwise():
    cube.apply_move(FCC)
    assert check_cube(FCC_CUBE, cube) == True
    cube.undo_move(FCC)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_back_clockwise():
    cube.apply_move(BC)
    assert check_cube(BC_CUBE, cube) == True
    cube.undo_move(BC)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_back_counter_clockwise():
    cube.apply_move(BCC)
    assert check_cube(BCC_CUBE, cube) == True
    cube.undo_move(BCC)
    assert check_cube(SOLVED_CUBE, cube) == True

def test_wrong_move():
    cube.apply_move("Nonsense")
    assert check_cube(SOLVED_CUBE, cube) == True


#--------------------------------------------------------------
# Test cases for the Rubiks Class general functions

def test_initialize_cube():
    assert check_cube(UNSOLVED_CUBE, unsolved_cube) == True


def test_is_solved():
    assert cube.is_solved() == True
    cube.apply_move(RVU)
    assert cube.is_solved() == False
    cube.undo_move(RVU)





    
