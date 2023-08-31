from crontab import CronTab

def remove_all_cronjobs(username):
    cron = CronTab(user='opc')
    cron.remove_all()
    cron.write()

if __name__ == '__main__':
    remove_all_cronjobs('opc')  # Replace with the desired username