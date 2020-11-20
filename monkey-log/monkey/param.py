import sys
import os
import json
import requests

MONKEY_PROJECT_ZONE = os.environ.get("MONKEY_PROJECT_ZONE", None)
MONKEY_CLIENT_PORT = 9991
MONKEY_CONFIG_MAX_RETRIES = 5

MONKEY_PROJECT_ZONE = ''  # temporary hack, since monkey does not set the env variable

def init(config=None, **kwargs):
    """
    Initialize the Monkey run. Specify the run config hyperparameters so they
    can be logged to Monkey client, and collected by Monkey core for
    visualization. When run locally, checks config validity only.

    config: dict of config hyperparameters
    kwargs: additional hyperparameters may be specified here
    """
    config = config or {}
    if not isinstance(config, dict):
        raise TypeError('config is not a dict')
    config.update(kwargs)

    # Serialize parameters
    try:
        json.dumps(config)
    except TypeError as e:
        raise TypeError('Run config must be JSON serializable') from e

    if MONKEY_PROJECT_ZONE is None:
        print('Monkey: detecting local test-run', file=sys.stderr)
        return

    # Post config to Monkey-client
    s = requests.Session()
    s.mount('http://', requests.adapters.HTTPAdapter(max_retries=MONKEY_CONFIG_MAX_RETRIES))
    try:
        r = s.put(f'http://localhost:{MONKEY_CLIENT_PORT}/config', json=config)
        r.raise_for_status()
    except requests.exceptions.RequestException:
        print('Monkey: config send failed; raising and exiting.', file=sys.stderr)
        raise
