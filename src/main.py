import json
import os
from datetime import datetime
from fastapi import FastAPI, Request

app = FastAPI()

# Ensure the logs directory exists
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

@app.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()

    try:
        # Ensure logs directory exists
        os.makedirs(LOG_DIR, exist_ok=True)

        # Generate timestamped log file to prevent overwriting
        timestamp = datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        log_filename = os.path.join(LOG_DIR, f"webhook_log_{timestamp}.json")

        # Save webhook event logs
        with open(log_filename, "w") as f:
            json.dump(payload, f, indent=4)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "received"}
