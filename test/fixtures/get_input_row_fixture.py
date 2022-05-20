from src.models.input_row import InputRow


def get_input_row(dt, count) -> InputRow:
  return InputRow(
    window_datetime = dt,
    window_count = count
  )
