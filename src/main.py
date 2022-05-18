import logging
from lib.utils import read_files
from models.input import Input
from transformers.input_row_transformer import row_to_input_row
from transformers.input_transformer import input_rows_to_input

DATA_DIR = "./data/"

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logging.info("Starting Traffic Counter...")

line_rows = []
data_lines = read_files(dir=DATA_DIR)
for line in data_lines:
  line_row = row_to_input_row(line)
  line_rows.append(line_row)

line_output = input_rows_to_input(line_rows)
logging.debug(line_output)

logging.info("Stopping Traffic Counter...")
