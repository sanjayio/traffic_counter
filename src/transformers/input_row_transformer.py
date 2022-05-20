from src.lib.utils import list_parse_map
from src.models.input_row import InputRow

def row_to_input_row(
  row_str: str
) -> InputRow: 
  return InputRow(
    **list_parse_map(row_str.split(" "))
  )
