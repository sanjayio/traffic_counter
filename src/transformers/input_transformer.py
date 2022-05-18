from typing import List
from models.input import Input
from models.input_row import InputRow


def input_rows_to_input(
  input_rows: List[InputRow]
) -> Input: 
  return Input(
    **{ "windows": input_rows }
  )