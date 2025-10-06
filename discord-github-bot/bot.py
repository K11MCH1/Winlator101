import requests
import time
import json
import os

# Config via environment variables
UPSTREAM_REPO = os.environ.get("FEX-Emu/FEX")       # e.g. FEX-Emu/FEX
DISCORD_WEBHOOK = os.environ.get("FEXEMU_WEBHOOK")   # your Discord webhook URL
INTERVAL = int(os.environ.get("INTERVAL", "60"))      # seconds between checks
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")         # optional, for higher API rate limit

STATE_FILE = "state.json"

HEADERS = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}

# Load last seen state
if os.path.exists(STATE_FILE):
    with open(STATE_FILE) as f:
        state = json.load(f)
else:
    state = {"last_commit": None, "pr_ids": [], "last_run_id": None}

def send_discord(msg):
    requests.post(DISCORD_WEBHOOK, json={"content": msg})

def get_latest_commit():
    r = requests.get(f"https://api.github.com/repos/{UPSTREAM_REPO}/commits/main", headers=HEADERS)
    r.raise_for_status()
    return r.json()["sha"]

def get_open_prs():
    r = requests.get(f"https://api.github.com/repos/{UPSTREAM_REPO}/pulls?state=open", headers=HEADERS)
    r.raise_for_status()
    return [(pr["id"], pr["html_url"]) for pr in r.json()]

def get_latest_successful_workflow():
    r = requests.get(f"https://api.github.com/repos/{UPSTREAM_REPO}/actions/runs?status=completed&conclusion=success&per_page=1", headers=HEADERS)
    r.raise_for_status()
    runs = r.json()["workflow_runs"]
    if runs:
        return runs[0]["id"], runs[0]["html_url"]
    return None, None

while True:
    try:
        # Check new commit
        commit = get_latest_commit()
        if commit != state.get("last_commit"):
            send_discord(f"New commit: https://github.com/{UPSTREAM_REPO}/commit/{commit}")
            state["last_commit"] = commit

        # Check new PRs
        prs = get_open_prs()
        for pr_id, pr_url in prs:
            if pr_id not in state.get("pr_ids", []):
                send_discord(f"New PR: {pr_url}")
                state.setdefault("pr_ids", []).append(pr_id)

        # Check new successful workflow run
        run_id, run_url = get_latest_successful_workflow()
        if run_id and run_id != state.get("last_run_id"):
            send_discord(f"Workflow succeeded: {run_url}")
            state["last_run_id"] = run_id

        # Save state
        with open(STATE_FILE, "w") as f:
            json.dump(state, f)
    except Exception as e:
        print("Error:", e)

    time.sleep(INTERVAL)
