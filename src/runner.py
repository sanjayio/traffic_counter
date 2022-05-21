import logging
from datetime import datetime
from src.lib.utils import read_files
from src.transformers.input_row_transformer import row_to_input_row
from src.transformers.input_transformer import input_rows_to_input

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)


class Runner:
  DATA_DIR = "./data/"

  def __init__(self):
    logging.info("Starting Traffic Counter...")
    self.data = None
    self.processed_at = None
    self._read()

  def _read(self):
    # Read all files in the DATA_DIR. 
    data_rows = read_files(dir=Runner.DATA_DIR)
    # Transform all text into input model. 
    input_rows = []
    for row in data_rows:
      input_row = row_to_input_row(row)
      input_rows.append(input_row)
    self.data = input_rows_to_input(input_rows)
    self.processed_at = datetime.now()
    logging.info("Finished reading files.")

  def get_total_cars(self):
    sum = 0
    for input_row in self.data.windows:
      sum += input_row.window_count
    return sum
  
  def get_daily_counts(self):
    res = {}
    for input_row in self.data.windows:
      input_date = str(input_row.window_datetime.date())
      if input_date in res:
        res[input_date] += input_row.window_count
      else:
        res[input_date] = input_row.window_count
    return res
  
  def get_top_3_half_hours(self):
    sorted_by_count_list = sorted(self.data.windows, key=lambda x: x.window_count, reverse=True)
    top_3_sorted_list = sorted_by_count_list[:3]
    sorted_windows = []
    for window in top_3_sorted_list:
      sorted_windows.append(
        f"{window.window_datetime.isoformat()} {window.window_count}"
      )
    return sorted_windows
  
  def get_1_5_hours_with_least_cars(self):
    sorted_by_dt_list = sorted(self.data.windows, key=lambda x: x.window_datetime)
    lowest_count = sorted(self.data.windows, key=lambda x: x.window_count, reverse=True)[0].window_count
    curr_count = 0
    curr_trio = []
    lowest_trio = []
    for i in range(len(sorted_by_dt_list)):
      for j in range(i, min(i + 3, len(sorted_by_dt_list))):
        curr_count += sorted_by_dt_list[j].window_count
        curr_trio.append(sorted_by_dt_list[j].window_datetime.isoformat())
      if curr_count <= lowest_count:
        lowest_count = curr_count
        lowest_trio = curr_trio if len(curr_trio) == 3 else lowest_trio
      curr_count = 0
      curr_trio = []
    return lowest_trio

  def __del__(self):
    logging.info("Stopping Traffic Counter...")
