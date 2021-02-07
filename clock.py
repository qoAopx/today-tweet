from apscheduler.schedulers.blocking import BlockingScheduler
import words
from datetime import datetime

twische = BlockingScheduler()

@twische.scheduled_job('interval',minutes=60)
def timed_job():
    today = datetime.now()
    if today.hour == 8 :
        words.puttweet()

if __name__ == "__main__":
    twische.start()