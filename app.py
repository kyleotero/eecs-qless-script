from flask import Flask, render_template, request
from crontab import CronTab
import os
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    success_modal = False
    if request.method == 'POST':
        global FIRST_NAME, LAST_NAME, PHONE_NUM, STUDENT_NUM, EMAIL, SERVICE_BTN_ID
        FIRST_NAME = request.form['first_name']
        LAST_NAME = request.form['last_name']
        PHONE_NUM = request.form['phone_num']
        STUDENT_NUM = request.form['student_num']
        EMAIL = request.form['email']
        SERVICE_BTN_ID = request.form['service_btn_id']

        schedule_cron_job()
        success_modal = True

    return render_template('index.html', show_modal=success_modal)

def schedule_cron_job():
    today = datetime.datetime.now()
    # if day of week is Friday, Saturday, or Sunday, set the cron job to run on the next monday
    if today.weekday() in [4, 5, 6]:
        run_date = today + datetime.timedelta(days=(7 - today.weekday()))
    else:
        run_date = today

    cron_command = f'/usr/bin/python3 /home/ubuntu/eecs-qless-script/bot.py {FIRST_NAME} {LAST_NAME} {PHONE_NUM} {STUDENT_NUM} {EMAIL} {SERVICE_BTN_ID}'
    cron = CronTab(user='ubuntu')

    cron_minute = '0'
    cron_hour = '9'
    cron_day = run_date.day
    cron_month = run_date.month
    cron_day_of_week = '*'

    job = cron.new(command=cron_command)
    job.setall(f'{cron_minute} {cron_hour} {cron_day} {cron_month} {cron_day_of_week}')

    print(job, flush=True)
    print(cron_command, flush=True)
    print("\n")
    cron.write()

if __name__ == '__main__':
    app.run()
