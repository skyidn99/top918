
from fastapi import FastAPI
import requests

app = FastAPI()

BLOCKLIST_URL = "https://raw.githubusercontent.com/Skiddle-ID/blocklist/main/domains.txt"

blocklist = set()

def load_blocklist():
    global blocklist
    r = requests.get(BLOCKLIST_URL)
    if r.status_code == 200:
        blocklist = set(line.strip().lower() for line in r.text.splitlines())

@app.on_event("startup")
def startup_event():
    load_blocklist()

@app.get("/check")
def check_domain(domain: str):
    d = domain.strip().lower()
    return {
        "domain": d,
        "blocked": d in blocklist,
        "source": "Skiddle-ID/blocklist"
    }
