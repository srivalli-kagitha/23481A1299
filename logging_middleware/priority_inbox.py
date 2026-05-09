import requests
from datetime import datetime
import heapq

# -------------------------------
# CONFIGURATION
# -------------------------------

API_URL = "http://4.224.186.213/evaluation-service/notifications"

# ✅ UPDATED HEADERS
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJNYXBDbGFpbXMiOnsiYXVkIjoiaHR0cDovLzIwLjI0NC41Ni4xNDQvZXZhbHVhdGlvbi1zZXJ2aWNlIiwiZW1haWwiOiJzcml2YWxsaWthZ2l0aGEwMUBnbWFpbC5jb20iLCJleHAiOjE3NzgzMDc3NTgsImlhdCI6MTc3ODMwNjg1OCwiaXNzIjoiQWZmb3JkIE1lZGljYWwgVGVjaG5vbG9naWVzIFByaXZhdGUgTGltaXRlZCIsImp0aSI6IjlhNGY4MGMzLTI3ZmItNDNiMi1hYTAyLTU2ODE2YWM5ZTNiZCIsImxvY2FsZSI6ImVuLUlOIiwibmFtZSI6ImthZ2l0aGEgc3JpdmFsbGkiLCJzdWIiOiI1ZWZiNjkxYy0xYTgzLTQ5ZDEtYjgxOC0zYmNiOWRkMWU4NzMifSwiZW1haWwiOiJzcml2YWxsaWthZ2l0aGEwMUBnbWFpbC5jb20iLCJuYW1lIjoia2FnaXRoYSBzcml2YWxsaSIsInJvbGxObyI6IjIzNDgxYTEyOTkiLCJhY2Nlc3NDb2RlIjoiZUpkQ3VDIiwiY2xpZW50SUQiOiI1ZWZiNjkxYy0xYTgzLTQ5ZDEtYjgxOC0zYmNiOWRkMWU4NzMiLCJjbGllbnRTZWNyZXQiOiJhSmtlYWRqdmhFRXNUbnF4In0.VeEbzQoFwt1TCHCJo5AYB_JR_Ul2tR1053uTO7p27Fs",
    "Content-Type": "application/json"
}

TOP_N = 10

# -------------------------------
# PRIORITY WEIGHTS
# -------------------------------

TYPE_WEIGHT = {
    "Placement": 3,
    "Result": 2,
    "Event": 1
}

# -------------------------------
# FETCH NOTIFICATIONS
# -------------------------------

def fetch_notifications():
    response = requests.get(API_URL, headers=HEADERS)

    print("Status Code:", response.status_code)

    # ✅ If API works
    if response.status_code == 200:
        data = response.json()
        return data.get("notifications", [])

    # ✅ If API fails → use fallback data
    print("API unavailable. Using sample notifications.")

    return [
        {
            "ID": "1",
            "Type": "Placement",
            "Message": "Google Hiring Drive",
            "Timestamp": "2026-04-25 10:00:00"
        },
        {
            "ID": "2",
            "Type": "Result",
            "Message": "Mid-Sem Results Published",
            "Timestamp": "2026-04-22 17:30:00"
        },
        {
            "ID": "3",
            "Type": "Event",
            "Message": "Hackathon Registration Open",
            "Timestamp": "2026-04-20 09:00:00"
        }
    ]

# -------------------------------
# CALCULATE PRIORITY SCORE
# -------------------------------

def calculate_priority(notification):

    weight = TYPE_WEIGHT.get(notification.get("Type"), 0)

    timestamp_str = notification.get(
        "Timestamp", "2000-01-01 00:00:00"
    )

    timestamp = datetime.strptime(
        timestamp_str,
        "%Y-%m-%d %H:%M:%S"
    )

    recency_score = timestamp.timestamp()

    return weight * 1_000_000_000 + recency_score


# -------------------------------
# MAINTAIN TOP N USING MIN HEAP
# -------------------------------

def get_top_notifications(notifications):

    heap = []

    for n in notifications:

        score = calculate_priority(n)

        if len(heap) < TOP_N:
            heapq.heappush(heap, (score, n))
        else:
            if score > heap[0][0]:
                heapq.heappushpop(heap, (score, n))

    return sorted(heap, reverse=True)


# -------------------------------
# DISPLAY OUTPUT
# -------------------------------

def display_notifications(top_notifications):

    print("\n===== PRIORITY INBOX (TOP 10) =====\n")

    for rank, (_, n) in enumerate(top_notifications, start=1):
        print(
            f"{rank}. [{n['Type']}] {n['Message']} - {n['Timestamp']}"
        )


# -------------------------------
# MAIN PROGRAM
# -------------------------------

if __name__ == "__main__":

    print("Fetching notifications...")

    notifications = fetch_notifications()

    print("Total Notifications Received:", len(notifications))

    if not notifications:
        print("No notifications received.")
    else:
        top_notifications = get_top_notifications(notifications)
        display_notifications(top_notifications)