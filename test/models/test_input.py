from datetime import datetime
from pydantic import ValidationError
from src.models.input import Input
from test.fixtures.get_input_fixture import get_input
from test.fixtures.get_input_row_fixture import get_input_row
import pytest


def test_param_valid() -> None:
  test_win = [get_input_row(datetime.now(), 5)]
  assert isinstance(get_input(test_win), Input), \
    f"expected type: {type(Input)}, got: {type(get_input(test_win))}"

def test_param_invalid() -> None:
  test_win = "test_win"
  with pytest.raises(ValidationError):
    get_input(test_win)
