from flask import Flask
app = Flask(__name__)

import os
import time
import threading

STATE_INITIAL = "state_initial"
STATE_STARTUP_SCRIPT = "state_startup_script"
STATE_STARTUP_SCRIPT_DONE = 'state_stateup_script_done'
STATE_MOUNTFS = "state_mount_fs"
STATE_RUN_CMD = "state_run_cmd"
state = STATE_INITIAL

@app.route('/ping')
def ping():
    return 'pong!'


@app.route('/state')
def get_state():
    global state
    return state

@app.route('/logs')
def get_logs():
    logs = "unable to open"
    with open('/var/log/monkey-client.log', 'r') as log_file:
        logs = log_file.read()
    return logs


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
    app.run(host='0.0.0.0', port=9991)
    
