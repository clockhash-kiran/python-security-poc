import json
import os
from fastapi import FastAPI, Request

app = FastAPI()

# Ensure the logs directory exists
os.makedirs("logs", exist_ok=True)

@app.post("/webhook")
async def webhook_listener(request: Request):
    payload = await request.json()

    try:
        # Ensure the logs directory exists inside Docker
        os.makedirs("logs", exist_ok=True)
        
        # Save webhook event logs
        with open("logs/webhook_log.json", "w") as f:
            json.dump(payload, f, indent=4)
    except Exception as e:
        return {"error": str(e)}

    return {"status": "received"}
