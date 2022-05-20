from pydantic import BaseModel
from typing import List
from src.models.input_row import InputRow

class Input(BaseModel, frozen=True):
  windows: List[InputRow]
