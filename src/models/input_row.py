from datetime import datetime
from pydantic import BaseModel, StrictInt

class InputRow(BaseModel, frozen=True):
  window_datetime: datetime
  window_count: StrictInt
