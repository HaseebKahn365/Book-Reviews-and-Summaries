import pkgutil
import json

__all__ = ['run_process']

def _internal_helper():
    return "This is an internal function"

def _load_config():
    raw_data = pkgutil.get_data(__package__, 'config.json')
    return json.loads(raw_data.decode('utf-8'))

def run_process():
    config = _load_config()
    print(f"Running with config: {config}")
    helper_msg = _internal_helper()
    print(f"Processing data with settings: {config.get('settings', {})}")
    return config
