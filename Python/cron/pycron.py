from flask import Flask, request, jsonify
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
import subprocess
import datetime
import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor

app = Flask(__name__)
scheduler = BackgroundScheduler()

def cron_job_function():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Cron job running at {current_time}")

@app.route('/schedule_cron', methods=['POST'])
def schedule_cron():
    data = request.get_json()
    cron_expression = data.get('cron_expression', None)

    if cron_expression:
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
    scheduler.start()
    app.run(debug=True)
