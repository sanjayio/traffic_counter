import logging
from typing import Dict, List
from models.input import Input
from models.input_row import InputRow

def list_to_map(input: List) -> Dict:
  iterator = iter(input)
  res_dct = dict(zip(iterator, iterator))
  return res_dct

sample_data = "2021-12-01T05:00:00 5".split(" ")
print(list_to_map(sample_data))
