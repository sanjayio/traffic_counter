import logging
from datetime import datetime
from lib.utils import read_files
from transformers.input_row_transformer import row_to_input_row
from transformers.input_transformer import input_rows_to_input

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

  def __del__(self):
    logging.info("Stopping Traffic Counter...")
