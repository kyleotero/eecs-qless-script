from crontab import CronTab
import os

def schedule_cronjob(script_path, username):
    cron = CronTab(user=username)
    job = cron.new(command=f'/usr/bin/python3 {script_path}')
    job.setall('30 9 * * *')  # schedule for 9:30 AM
    cron.write()

def remove_all_cronjobs(username):
    cron = CronTab(user=username)
    cron.remove_all()
    cron.write()

if __name__ == '__main__':
    script_path = os.path.abspath(__file__)
    username = 'ubuntu'

    remove_all_cronjobs(username)
    schedule_cronjob(script_path, username)
