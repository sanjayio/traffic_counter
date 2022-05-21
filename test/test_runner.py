from unittest import TestCase
from unittest.mock import patch
import src
from src.runner import Runner

  
@patch('src.runner.Runner')
def test_runner(mocked_runner):
  src.runner.Runner()
  assert mocked_runner is src.runner.Runner
  assert mocked_runner.called
