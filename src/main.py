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

  # 3. The top 3 half hours with most cars, in the same format as the input file
  sorted_by_count_list = sorted(data, key=lambda x: x.window_count, reverse=True)
  top_3_sorted_list = sorted_by_count_list[:3]
  sorted_windows = []
  for window in top_3_sorted_list:
    sorted_windows.append(
      f"{window.window_datetime.isoformat()} {window.window_count}"
    )
  logging.debug(f"The top 3 half hours with most cars: {sorted_windows}")

  # 4. The 1.5 hour period with least cars (i.e. 3 contiguous half hour records)
  sorted_by_dt_list = sorted(data, key=lambda x: x.window_datetime)
  lowest_count = sorted_by_count_list[0].window_count
  curr_count = 0
  curr_trio = []
  lowest_trio = []
  for i in range(len(sorted_by_dt_list)):
    for j in range(i, min(i + 3, len(sorted_by_dt_list))):
      curr_count += sorted_by_dt_list[j].window_count
      curr_trio.append(sorted_by_dt_list[j].window_datetime.isoformat())
    if curr_count <= lowest_count:
      lowest_count = curr_count
      lowest_trio = curr_trio if len(curr_trio) == 3 else lowest_trio
    curr_count = 0
    curr_trio = []
  logging.debug(f"The 1.5 hour period with least cars: {lowest_trio}")

if __name__ == "__main__":
  main()




