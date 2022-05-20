from typing import List
from src.models.input import Input
from src.models.input_row import InputRow


def input_rows_to_input(
  input_rows: List[InputRow]
) -> Input: 
  return Input(
    **{ "windows": input_rows }
  )