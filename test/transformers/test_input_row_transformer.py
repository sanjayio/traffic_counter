from src.models.input_row import InputRow
from src.transformers.input_row_transformer import row_to_input_row
import pytest

def test_valid_row_to_input_row():
  test_row = "2021-12-01T05:00:00 5"
  assert isinstance(row_to_input_row(test_row), InputRow), \
    f"expected type: {type(InputRow)}, got: {type(row_to_input_row(test_row))}"

def test_invalid_row_to_input_row():
  test_row = "invalid"
  with pytest.raises(ValueError):
    row_to_input_row(test_row)
