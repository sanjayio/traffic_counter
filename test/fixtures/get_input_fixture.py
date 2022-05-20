from src.models.input import Input
from datetime import datetime
from test.fixtures.get_input_row_fixture import get_input_row

def get_input(win) -> Input:
  return Input(
    windows = win
  )
