import requests

BASE_URL = "http://127.0.0.1:8000"


def decide_action(state):
    # simple rule-based logic (safe & deterministic)

    if state["urgency"] >= 7:
        return "escalate"

    if state["customer_type"] == "premium" and state["urgency"] >= 5:
        return "escalate"

    if state["sentiment"] == "angry":
        return "reply"

    return "ignore"


def run_episode():
    # reset environment
    res = requests.get(f"{BASE_URL}/reset")
    state = res.json()["state"]

    action = decide_action(state)

    # take step
    res = requests.post(f"{BASE_URL}/step", json={"action": action})
    data = res.json()

    return data["reward"]


def main():
    total_score = 0
    runs = 5  # run multiple times

    for i in range(runs):
        score = run_episode()
        print(f"Run {i+1}: Score = {score}")
        total_score += score

    avg_score = total_score / runs
    print("\nAverage Score:", round(avg_score, 2))


if __name__ == "__main__":
    main()