from typing import List
from models.input import Input
from get_input_row_fixture import get_input_row

def get_input() -> Input:
  return Input(
    windows = List(get_input_row())
  )
