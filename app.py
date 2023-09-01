from flask import Flask, render_template, request
from crontab import CronTab
import os

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
    cron_command = f'/usr/bin/python3 /home/ubuntu/eecs-qless-script/bot.py {FIRST_NAME} {LAST_NAME} {PHONE_NUM} {STUDENT_NUM} {EMAIL} {SERVICE_BTN_ID}'
    cron = CronTab(user='ubuntu')

    job = cron.new(command=cron_command)
    job.setall('0 9 * * *')

    print(cron_command, flush=True)
    cron.write()

if __name__ == '__main__':
    app.run()
