# app.py
import datetime
import subprocess
from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor
from flask_migrate import Migrate
from flask_apscheduler import APScheduler

app = Flask(__name__)
scheduler = BackgroundScheduler()

flask_apscheduler = APScheduler()
flask_apscheduler.init_app(app)

def cron_job_function():
    script_path = '/home/jimmycooks/scripts/cool_report.py'
    subprocess.run(['python3', script_path])
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Cron job running at {current_time}")

# Add SQLAlchemyJobStore and ThreadPoolExecutor
jobstores = {
    'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
}
executors = {
    'default': ThreadPoolExecutor(10)
}


# Clear jobs from the database
jobstore = SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
jobstore.remove_all_jobs()

scheduler.configure(jobstores=jobstores, executors=executors)

@app.route('/schedule_cron', methods=['POST'])
def schedule_cron():
    data = request.get_json()
    cron_expression = data.get('cron_expression', None)

    if cron_expression:
        # Check if a similar cron job already exists
        existing_jobs = scheduler.get_jobs(jobstore='default')
        for job in existing_jobs:
            if job.trigger.__str__() == cron_expression:
                return jsonify({'message': f'Cron job already scheduled with expression: {cron_expression}'}), 200
        
        # Add the cron job with the specified expression
        trigger = CronTrigger.from_crontab(cron_expression)
        scheduler.add_job(cron_job_function, trigger=trigger)
        return jsonify({'message': f'Cron job scheduled successfully with expression: {cron_expression}'}), 200
    else:
        return jsonify({'error': 'Invalid request. Missing cron_expression parameter'}), 400

@app.route('/unschedule_cron', methods=['POST'])
def unschedule_cron():
    # Remove all cron jobs
    scheduler.remove_all_jobs()
    return jsonify({'message': 'All cron jobs unscheduled successfully'}), 200

if __name__ == '__main__':
    # Add the following line to enable the dashboard
    scheduler.start()
    #flask_apscheduler.start()
    app.run(debug=True, use_reloader=False)
