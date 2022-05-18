import logging
from lib.utils import list_parse_map, read_files
from models.input import Input
from models.input_row import InputRow

DATA_DIR = "./data/"

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logging.info("Starting Traffic Counter...")

line_rows = []
data_lines = read_files(dir=DATA_DIR)
for line in data_lines:
  line_data = line.split(" ")
  line_map = list_parse_map(line_data)
  line_row = InputRow(**line_map)
  line_rows.append(line_row)

line_output = Input(**{"windows": line_rows})
logging.debug(line_output)

logging.info("Stopping Traffic Counter...")
