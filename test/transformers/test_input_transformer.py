from datetime import datetime
from src.models.input import Input
from src.transformers.input_transformer import input_rows_to_input
from test.fixtures.get_input_row_fixture import get_input_row
import pytest


def test_valid_row_to_input_row():
  test_input_rows = [get_input_row(datetime.now(), 5)]
  assert isinstance(input_rows_to_input(test_input_rows), Input), \
    f"expected type: {type(Input)}, got: {type(input_rows_to_input(test_input_rows))}"

def test_invalid_row_to_input_row():
  test_input_rows = "invalid_input_rows"
  with pytest.raises(ValueError):
    input_rows_to_input(test_input_rows)
