import logging
from lib.utils import list_parse_map
from models.input import Input
from models.input_row import InputRow

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.DEBUG)
logging.info("Starting Traffic Counter...")

sample_data = "2021-12-01T05:00:00 5".split(" ")
sample_map = list_parse_map(sample_data)

sample_row = InputRow(**sample_map)
sample_output = Input(**{"windows": [sample_row]})
logging.debug(sample_output)

logging.info("Stopping Traffic Counter...")
