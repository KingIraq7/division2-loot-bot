import requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1509148612980904068/SotUQNd0clRG-5gn25CCNIDBQEA9_HGUGzG6vIF42y0uLjj5aR3AINXion1mmXGzyk7K"

url = "https://hi-dep.github.io/division2/?view=event&lang=en"

message = f"🎯 Division 2 Escalation Loot Today\n\n{url}"

requests.post(WEBHOOK_URL, json={
    "content": message
})

print("Sent!")
