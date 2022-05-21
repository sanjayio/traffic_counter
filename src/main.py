from runner import *

def main() -> None:
  # Initialize runner and get data
  runner = Runner()

  logging.debug(f"Total cars: {runner.get_total_cars()}")
  logging.debug(f"Cars seen per day: {runner.get_daily_counts()}")
  logging.debug(f"The top 3 half hours with most cars: {runner.get_top_3_half_hours()}")
  logging.debug(f"The 1.5 hour period with least cars: {runner.get_1_5_hours_with_least_cars()}")

if __name__ == "__main__":
  main()
