from runner import *

def main() -> None:
  # Initialize runner and get data
  runner = Runner()
  data = runner.data.windows
  
  # Answering questions
  # 1. The number of cars seen in total
  sum = 0
  for input_row in data:
    sum += input_row.window_count
  logging.debug(f"The number of cars seen in total: {sum}")

  # 2. A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the
  # number of cars seen on that day (eg. 2016-11-23 289) for all days listed in the input file.
  res = {}
  for input_row in data:
    input_date = str(input_row.window_datetime.date())
    if input_date in res:
      res[input_date] += input_row.window_count
    else:
      res[input_date] = input_row.window_count
  logging.debug(f"A sequence of lines where each line contains a date (in yyyy-mm-dd format) and the number of cars seen on that day: \n {res}")



if __name__ == "__main__":
  main()




