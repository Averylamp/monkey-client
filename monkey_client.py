from flask import Flask, jsonify
application = Flask(__name__)

import os
import time
import threading
import json

STATE_INITIAL = "state_initial"
STATE_STARTUP_SCRIPT = "state_startup_script"
STATE_STARTUP_SCRIPT_DONE = 'state_stateup_script_done'
STATE_MOUNTFS = "state_mount_fs"
STATE_RUN_CMD = "state_run_cmd"
state = STATE_INITIAL

MONKEY_INSTANCE_PROJECT = None
MONKEY_INSTANCE_ZONE    = None
MONKEY_INSTANCE_NAME    = os.uname()[1]
project_zone_string = os.environ.get("MONKEY_PROJECT_ZONE", None)
if project_zone_string:
    MONKEY_INSTANCE_PROJECT = project_zone_string.split("/")[1]
    MONKEY_INSTANCE_ZONE = project_zone_string.split("/")[3]

# Machine info helps to give
machine_info = dict()

@application.route('/ping')
def ping():
    return 'pong!'

@application.route('/info')
def get_info():
    global MONKEY_INSTANCE_PROJECT, \
        MONKEY_INSTANCE_ZONE, \
        MONKEY_INSTANCE_NAME
    return jsonify({
        "machine_name": MONKEY_INSTANCE_NAME,
        "machine_project": MONKEY_INSTANCE_PROJECT,
        "machine_zone" : MONKEY_INSTANCE_ZONE
    })

@application.route('/state')
def get_state():
    global state
    return state

@application.route('/log')
@application.route('/logs')
def get_logs():
    def logs():
        with open('/var/log/monkey-client.log', 'r') as log_file:
            while True:
                yield log_file.read()
                time.sleep(1)
    return application.response_class(logs(), mimetype='text/plain')

@application.route('/startup-log')
@application.route('/startup-logs')
def get_startup_logs():
    def logs():
        with open('/var/log/startup-script.log', 'r') as log_file:
            while True:
                yield log_file.read()
                time.sleep(1)
    return application.response_class(logs(), mimetype='text/plain')


def state_loop():
    global state
    if state == STATE_INITIAL or state == STATE_STARTUP_SCRIPT:
        try:
            f = open("/startup-script.lock")
            state = STATE_STARTUP_SCRIPT
            f.close()
        except IOError:
            if state == STATE_STARTUP_SCRIPT:
                state = STATE_STARTUP_SCRIPT_DONE


    threading.Timer(1.0, state_loop).start()

if __name__ == '__main__':
    state_loop()
    application.run(host='0.0.0.0', port=9991)

