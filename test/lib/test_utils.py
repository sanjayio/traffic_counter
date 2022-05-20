from datetime import datetime
from unittest.mock import patch
import src
from src.lib.utils import list_parse_map, flatten

def test_list_parse_map():
  test_input = ["2021-12-01T05:00:00", "5"]
  expected_output = {
    "window_datetime": datetime.strptime("2021-12-01T05:00:00", "%Y-%m-%dT%H:%M:%S"),
    "window_count": 5
  }
  assert list_parse_map(test_input) == expected_output

def test_flatten():
  test_input = ["1", ["2", "3"]]
  expected_output = ["1", "2", "3"]
  assert flatten(test_input) == expected_output

@patch('src.lib.utils.read_files')
def test_read_files(mocked_read_files):
  test_input = "foo_dir"
  mocked_read_files(test_input)
  assert mocked_read_files.called
  assert mocked_read_files.called_with(test_input)
  assert mocked_read_files is src.lib.utils.read_files
