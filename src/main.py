import logging
from lib.utils import read_files
from transformers.input_row_transformer import row_to_input_row
from transformers.input_transformer import input_rows_to_input

DATA_DIR = "./data/"

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logging.info("Starting Traffic Counter...")

# Read all files in the DATA_DIR. 
data_rows = read_files(dir=DATA_DIR)

# Transform all text into input model. 
input_rows = []
for row in data_rows:
  input_row = row_to_input_row(row)
  input_rows.append(input_row)
input = input_rows_to_input(input_rows)

# Calculating necessary statistics:

# 1. The number of cars seen in total
sum = 0
for input_row in input.windows:
  sum += input_row.window_count
logging.debug(f"The number of cars seen in total: {sum}")

# 2. A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the
# number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file.
res = {}
for input_row in input.windows:
  input_date = str(input_row.window_datetime.date())
  if input_date in res:
    res[input_date] += input_row.window_count
  else:
    res[input_date] = input_row.window_count
logging.debug(f"A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the number of cars seen on that day: \n {res}")

logging.info("Stopping Traffic Counter...")
