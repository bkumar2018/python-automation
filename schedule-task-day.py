import schedule
import time

def morning_job():
    print("Good morning! Running at 9:30 AM...")

# Schedule the job every day at 9:30 AM
schedule.every().day.at("09:30").do(morning_job)

while True:
    schedule.run_pending()
    time.sleep(1)


# This example schedules a task to run every Monday:

# import schedule
# import time

# def weekly_job():
#     print("Running every Monday...")

# # Schedule the job to run every Monday
# schedule.every().monday.do(weekly_job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


# This example shows how to run a job every 2 hours:
# import schedule
# import time

# def hourly_job():
#     print("Job running every 2 hours...")

# # Schedule the job every 2 hours
# schedule.every(2).hours.do(hourly_job)

# while True:
#     schedule.run_pending()
#     time.sleep(1)



# You can also cancel a scheduled job after 15 seconds:
# import schedule
# import time

# def job():
#     print("This job runs every 5 seconds.")

# # Schedule the job every 5 seconds
# job_instance = schedule.every(5).seconds.do(job)

# # Run the scheduler for some time, then cancel the job
# start_time = time.time()

# while True:
#     schedule.run_pending()
#     if time.time() - start_time > 15:  # Cancel job after 15 seconds
#         schedule.cancel_job(job_instance)
#         print("Job canceled.")
#         break
#     time.sleep(1)

