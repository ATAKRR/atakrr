## File: sig_spawn/cli.py
import argparse
from .core import generate_signal

def main():
    parser = argparse.ArgumentParser(description="Signal Generator CLI")
    parser.add_argument('--config', type=str, required=True, help='Path to config file')
    args = parser.parse_args()

    generate_signal(args.config)

if __name__ == '__main__':
    main()


## File: sig_spawn/core.py
import json

def generate_signal(config_path):
    with open(config_path, 'r') as f:
        cfg = json.load(f)

    # Placeholder signal gen logic
    print(f"[+] Generating {cfg['modulation']} signal with SNR={cfg['snr']}")
    # Future: return IQ samples, apply manglers, save to .sigmf


## File: sig_spawn/tasks.py
from celery import Celery
from .core import generate_signal

app = Celery('sig_spawn', broker='redis://localhost:6379/0')

@app.task
def generate_task(config_path):
    return generate_signal(config_path)


## File: sig_spawn/api.py
from fastapi import FastAPI
from pydantic import BaseModel
from .tasks import generate_task

app = FastAPI()

class GenRequest(BaseModel):
    config_path: str

@app.post("/generate")
def generate(req: GenRequest):
    task = generate_task.delay(req.config_path)
    return {"task_id": task.id, "status": "queued"}


## File: sig_spawn/__init__.py
# makes it a package


## Example config file (mod_wifi.json)
{
  "modulation": "wifi",
  "snr": 20,
  "output_path": "wifi_sig_001.sigmf-data"
}


## Command to run worker:
# celery -A sig_spawn.tasks worker --loglevel=info

## Command to run API:
# uvicorn sig_spawn.api:app --reload
