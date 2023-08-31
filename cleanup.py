from crontab import CronTab

def remove_all_cronjobs(username):
    cron = CronTab(user='mohammad')
    cron.remove_all()
    cron.write()

if __name__ == '__main__':
    remove_all_cronjobs('mohammad')  # Replace with the desired username