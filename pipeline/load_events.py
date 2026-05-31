import json
import requests

with open(
    "data/generated_events.json",
    "r"
) as f:
    events = json.load(f)

response = requests.post(
    "http://127.0.0.1:8000/events/ingest",
    json=events
)

print(response.status_code)
print(response.json())