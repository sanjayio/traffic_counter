from pydantic import BaseModel
from typing import List
from models.input_row import InputRow

class Input(BaseModel, frozen=True):
  windows: List[InputRow]
