from pydantic import ValidationError
from src.models.input_row import InputRow
from test.fixtures.get_input_row_fixture import get_input_row
from datetime import datetime
import pytest


def test_both_params_valid() -> None:
  dt = datetime.now()
  cnt = 5
  assert isinstance(get_input_row(dt, cnt), InputRow), \
    f"expected type: {type(InputRow)}, got: {type(get_input_row(dt, cnt))}"

def test_one_invalid_param() -> None:
  dt = datetime.now()
  cnt = "5"
  with pytest.raises(ValidationError):
    get_input_row(dt, cnt)

def test_both_invalid_params() -> None:
  dt = "10"
  cnt = "5"
  with pytest.raises(ValidationError):
    get_input_row(dt, cnt)
