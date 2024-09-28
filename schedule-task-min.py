import schedule
import time

def job():
    print("This task runs every minute.")

schedule.every().minute.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)

