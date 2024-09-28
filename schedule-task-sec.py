import schedule
import time


def job():
    print("Job running every 10 seconds...")

# Schedule the job every 10 seconds
schedule.every(10).seconds.do(job)

# Run the scheduler in an infinite loop
while True:
    schedule.run_pending()
    time.sleep(1)