from ast import parse
from typing import Dict, List
from datetime import datetime
from models.input_row import InputRow


def list_parse_map(input: List) -> Dict:

  parse_dt = lambda x: datetime.strptime(x, "%Y-%m-%dT%H:%M:%S")
  parse_int = lambda x: int(x)

  keywords = ["window_datetime", "window_count"]
  parsed_input = [parse_dt(str(input[0])), parse_int(input[1])]

  input_iter = iter(parsed_input)
  keywords_iter = iter(keywords)
  res_dct = dict(zip(keywords_iter, input_iter))
  
  return res_dct
