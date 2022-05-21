from runner import *

def main() -> None:
  # Initialize runner and get data
  runner = Runner()

  logging.debug(f"🚗 : {runner.get_total_cars()} cars")
  logging.debug(f"🚗 per day : {runner.get_daily_counts()}")
  logging.debug(f"⏰ Top 3 half hours with most 🚗 : {runner.get_top_3_half_hours()}")
  logging.debug(f"⏰ 1.5 hour period with least 🚗 : {runner.get_1_5_hours_with_least_cars()}")

if __name__ == "__main__":
  main()
